import numpy as np
from dataclasses import dataclass, field

from .demosaic import demosaic_bilinear_rggb
from .color import apply_white_balance_rgb, apply_ccm, tone_map_reinhard
from .gamma import gamma_encode

@dataclass
class ISPConfig:
    wb_gains: tuple = (2.0, 1.0, 1.5)  # (R,G,B)
    ccm: np.ndarray = field(default_factory=lambda: np.eye(3, dtype=np.float32))
    gamma: float = 2.2
    tone_mapping: str = "reinhard"  # or "none"

def run_isp_rggb(bayer01: np.ndarray, cfg: ISPConfig):
    stages = {}

    # 1) Demosaic
    rgb = demosaic_bilinear_rggb(bayer01)
    stages["01_demosaic"] = rgb

    # 2) White balance
    rgb = apply_white_balance_rgb(rgb, cfg.wb_gains)
    stages["02_white_balance"] = rgb

    # 3) Color correction matrix
    rgb = apply_ccm(rgb, cfg.ccm.astype(np.float32))
    stages["03_ccm"] = rgb

    # 4) Tone mapping (optional)
    if cfg.tone_mapping == "reinhard":
        rgb = tone_map_reinhard(rgb)
        stages["04_tonemap"] = rgb
    else:
        stages["04_tonemap"] = rgb

    # 5) Gamma encode
    rgb = gamma_encode(rgb, cfg.gamma)
    stages["05_gamma"] = rgb

    return rgb, stages
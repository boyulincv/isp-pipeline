import numpy as np

def estimate_gray_world_gains(rgb01: np.ndarray, eps: float = 1e-6) -> tuple:
    """
    Estimate white balance gains using Gray World Assumption.
    Returns (r_gain, g_gain, b_gain).
    """
    rgb01 = np.clip(rgb01, 0.0, 1.0)

    r_avg = float(np.mean(rgb01[..., 0]))
    g_avg = float(np.mean(rgb01[..., 1]))
    b_avg = float(np.mean(rgb01[..., 2]))

    r_gain = g_avg / (r_avg + eps)
    g_gain = 1.0
    b_gain = g_avg / (b_avg + eps)

    return (r_gain, g_gain, b_gain)

def apply_white_balance_rgb(rgb01: np.ndarray, gains=(2.0, 1.0, 1.5)) -> np.ndarray:
    """
    gains: (r_gain, g_gain, b_gain)
    """
    r, g, b = gains
    out = rgb01.copy()
    out[..., 0] *= r
    out[..., 1] *= g
    out[..., 2] *= b
    return np.clip(out, 0.0, 1.0)

def apply_ccm(rgb01: np.ndarray, ccm: np.ndarray) -> np.ndarray:
    """
    ccm: 3x3 matrix, applied to RGB vectors.
    """
    h, w, _ = rgb01.shape
    flat = rgb01.reshape(-1, 3)
    out = flat @ ccm.T
    out = out.reshape(h, w, 3)
    return np.clip(out, 0.0, 1.0)


def tone_map_reinhard(rgb01: np.ndarray) -> np.ndarray:
    """
    Simple global Reinhard tone mapping on linear-ish RGB
    """
    #rgb01 = np.maximum(rgb01, 0.0)
    return rgb01 #(rgb01 / (1.0 + rgb01)).astype(np.float32)
import numpy as np
import cv2

def demosaic_bilinear_rggb(bayer01: np.ndarray) -> np.ndarray:
    """
    Input: single-channel Bayer in [0,1], float32
    Output: RGB in [0,1], float32
    """
    if bayer01.dtype != np.float32:
        bayer01 = bayer01.astype(np.float32)

    # OpenCV expects 8/16-bit for demosaic; use 16-bit to reduce quantization
    b16 = np.clip(bayer01 * 65535.0, 0, 65535).astype(np.uint16)

    # RGGB -> OpenCV demosaic gives BGR output
    bgr16 = cv2.cvtColor(b16, cv2.COLOR_BayerRG2BGR)

    rgb01 = (bgr16[..., ::-1].astype(np.float32) / 65535.0)
    return np.clip(rgb01, 0.0, 1.0)
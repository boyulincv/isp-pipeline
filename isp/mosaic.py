import numpy as np

def bgr_to_rgb_float01(img_bgr: np.ndarray) -> np.ndarray:
    # OpenCV is BGR; convert to RGB and normalize to [0,1]
    rgb = img_bgr[..., ::-1].astype(np.float32) / 255.0
    return rgb

def make_bayer_rggb(rgb01: np.ndarray) -> np.ndarray:
    """
    Create a single-channel Bayer mosaic (RGGB) from an RGB image.
    RGGB pattern:
      (0,0) R  (0,1) G
      (1,0) G  (1,1) B
    """
    h, w, _ = rgb01.shape
    bayer = np.zeros((h, w), dtype=np.float32)

    R = rgb01[..., 0]
    G = rgb01[..., 1]
    B = rgb01[..., 2]

    bayer[0::2, 0::2] = R[0::2, 0::2]  # R
    bayer[0::2, 1::2] = G[0::2, 1::2]  # G
    bayer[1::2, 0::2] = G[1::2, 0::2]  # G
    bayer[1::2, 1::2] = B[1::2, 1::2]  # B
    return bayer
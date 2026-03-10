import numpy as np

def inverse_gamma(rgb01: np.ndarray, gamma: float = 2.2) -> np.ndarray:
    """
    Convert gamma-encoded RGB image to linear RGB.
    """
    rgb01 = np.clip(rgb01, 0.0, 1.0)
    return np.power(rgb01, gamma).astype(np.float32)

def gamma_encode(rgb01: np.ndarray, gamma: float = 2.2) -> np.ndarray:
    # assume linear input, output is display-ish
    rgb01 = np.clip(rgb01, 0.0, 1.0)
    return np.power(rgb01, 1.0 / gamma).astype(np.float32)
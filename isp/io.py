import cv2
import numpy as np
from pathlib import Path

def read_bgr(path: str) -> np.ndarray:
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError(f"Cannot read image: {path}")
    return img

def write_bgr(path: str, img_bgr: np.ndarray) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    ok = cv2.imwrite(path, img_bgr)
    if not ok:
        raise IOError(f"Failed to write image: {path}")
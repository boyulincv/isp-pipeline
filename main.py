import argparse
import numpy as np

from isp.io import read_bgr, write_bgr
from isp.mosaic import bgr_to_rgb_float01, make_bayer_rggb
from isp.pipeline import ISPConfig, run_isp_rggb

def rgb01_to_bgr8(rgb01: np.ndarray) -> np.ndarray:
    rgb8 = (np.clip(rgb01, 0.0, 1.0) * 255.0 + 0.5).astype(np.uint8)
    bgr8 = rgb8[..., ::-1]
    return bgr8

def gray01_to_bgr8(gray01: np.ndarray) -> np.ndarray:
    g8 = (np.clip(gray01, 0.0, 1.0) * 255.0 + 0.5).astype(np.uint8)
    return np.stack([g8, g8, g8], axis=-1)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True, help="input image path (png/jpg)")
    ap.add_argument("--out", dest="out", required=True, help="output final image path")
    ap.add_argument("--save-stages", action="store_true", help="save intermediate stage images")
    ap.add_argument("--wb", type=str, default="2.0,1.0,1.5", help="white balance gains r,g,b")
    ap.add_argument("--gamma", type=float, default=2.2)
    args = ap.parse_args()

    wb = tuple(float(x) for x in args.wb.split(","))
    cfg = ISPConfig(wb_gains=wb, gamma=args.gamma)

    img_bgr = read_bgr(args.inp)
    rgb01 = bgr_to_rgb_float01(img_bgr)

    # simulate RAW Bayer (RGGB)
    bayer01 = make_bayer_rggb(rgb01)

    final_rgb01, stages = run_isp_rggb(bayer01, cfg)

    # save final
    write_bgr(args.out, rgb01_to_bgr8(final_rgb01))

    if args.save_stages:
        # save bayer visualization + stages
        write_bgr("results/00_bayer.png", gray01_to_bgr8(bayer01))
        for k, v in stages.items():
            write_bgr(f"results/{k}.png", rgb01_to_bgr8(v))

    print("Done.")
    print(f"Saved: {args.out}")
    if args.save_stages:
        print("Saved intermediate stages to results/")

if __name__ == "__main__":
    main()
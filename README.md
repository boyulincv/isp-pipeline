# isp-pipeline

This project implements a simplified Image Signal Processing (ISP) pipeline in Python.
It simulates a Bayer RGGB sensor from an RGB image and reconstructs the final RGB output through demosaicing, white balance, color correction, tone mapping, and gamma correction.

## Pipeline Includes

- Bayer mosaic simulation (RGGB)
- Demosaicing
- White balance
- Color correction matrix
- Tone mapping
- Gamma correction

## Quickstart

Install dependencies:

```bash
pip install -r requirements.txt
```

Place an input image at `data/input.png`, then run:

```bash
python main.py --in data/input.png --out results/final.png --save-stages
```

## ISP Pipeline

```mermaid
flowchart TD
A[Input RGB Image] --> B[Convert to float 0-1]
B --> C[Bayer Mosaic RGGB]
C --> D[Demosaicing Bilinear]
D --> E[White Balance]
E --> F[Color Correction Matrix]
F --> G[Tone Mapping]
G --> H[Gamma Correction]
H --> I[Convert to uint8 BGR]
I --> J[Final Image]
```

## Results

### Bayer Mosaic
![Bayer](results/00_bayer.png)

### Demosaiced Image
![Demosaic](results/01_demosaic.png)

### Final Output
![Final](results/final.png)

## Project Structure

isp-pipeline/
├── data/
├── isp/
│   ├── color.py
│   ├── demosaic.py
│   ├── io.py
│   ├── mosaic.py
│   └── pipeline.py
├── results/
├── main.py
├── requirements.txt
└── README.md
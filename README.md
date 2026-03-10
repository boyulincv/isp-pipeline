# isp-pipeline

This project implements a simplified Image Signal Processing (ISP) pipeline in Python.
It simulates a Bayer RGGB sensor from an RGB image and reconstructs the final RGB output through demosaicing, white balance, color correction, tone mapping, and gamma correction.

## Pipeline Includes

- Inverse Gamma (Linearization)
- Bayer mosaic simulation (RGGB)
- Demosaicing
- White balance
- Color correction matrix
- Tone mapping
- Gamma correction



## ISP Pipeline

```mermaid
flowchart TD
A[Input RGB Image] --> B[Convert to float 0-1]
B --> C[Inverse Gamma]
C --> D[Bayer Mosaic RGGB]
D --> E[Demosaicing Bilinear]
E --> F[White Balance]
F --> G[Color Correction Matrix]
G --> H[Tone Mapping]
H --> I[Gamma Correction]
I --> J[Convert to uint8 BGR]
J --> K[Final Image]
```

## Results
### Input
![Input](data/input.png)

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
│         ├── color.py  
│         ├── demosaic.py  
│         ├── io.py  
│         ├── mosaic.py  
│         └── pipeline.py  
├── results/  
├── main.py  
├── requirements.txt  
└── README.md  


## Quickstart

Install dependencies:

```bash
pip install -r requirements.txt
```

Place an input image at `data/input.png`, then run:

```bash
python main.py --in data/input.png --out results/final.png --save-stages --wb-mode gray_world
```
# sample_0016

## Reuse this sample when
- when you need to compare distributions across categories
- when medians, quartiles, and outliers matter
- when raw per-sample values are available instead of only means

## What pattern this script implements
This sample is a reusable template for a **boxplot for grouped score distributions**.

## Data shape expected by this script
- one raw observation per row
- a category key for grouping
- enough observations per category for quartiles to be meaningful

## How to adapt it
- replace the value rows in `distribution_measurements_v1.csv`
- change category order and colors in `plot.py`
- turn off fliers or add notches if the target style requires it

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/distribution_measurements_v1.csv`

## Figure group used here
- `model_score_distribution`

## Run this sample
From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 samples/distribution/sample_0016/plot.py
```

## Output path
```text
samples/distribution/sample_0016/output.png
```

## Do not use this sample when
- when distribution shape matters more than quartiles
- when there are too few observations per group for a boxplot to be informative

## Closest sibling samples
- `sample_0017`
- `sample_0018`

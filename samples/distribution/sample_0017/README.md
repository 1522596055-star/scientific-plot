# sample_0017

## Reuse this sample when
- when the full distribution shape matters more than quartiles alone
- when categories have enough observations to estimate density
- when a softer distribution-oriented view is preferred over a boxplot

## What pattern this script implements
This sample is a reusable template for a **violin plot for response distributions**.

## Data shape expected by this script
- many raw observations per category
- a category key for grouping
- continuous numeric response values

## How to adapt it
- replace the grouped values in `distribution_measurements_v1.csv`
- adjust bandwidth or violin styling if needed
- combine with overlaid points later if the target figure needs more detail

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/distribution_measurements_v1.csv`

## Figure group used here
- `cell_response_distribution`

## Run this sample
From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 samples/distribution/sample_0017/plot.py
```

## Output path
```text
samples/distribution/sample_0017/output.png
```

## Do not use this sample when
- when you only need a simple summary and a boxplot is enough
- when there are too few samples to estimate a stable violin shape

## Closest sibling samples
- `sample_0016`
- `sample_0018`

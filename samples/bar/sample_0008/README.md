# sample_0008

## Reuse this sample when
- when positive and negative sensitivities must be shown around zero
- when two conditions should be compared with the same bar layout
- when category names are long and work better on a horizontal axis

## What pattern this script implements
This sample is a reusable template for a **two-panel horizontal sensitivity bar chart**.

## Data shape expected by this script
- one row per variable per panel
- positive and negative values centered on zero
- category labels that should remain readable as y-axis text

## How to adapt it
- replace categories and values in `categorical_measurements_v1.csv`
- update x-axis limits to match your sensitivity range
- change panel titles while keeping the same left/right comparison layout

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/categorical_measurements_v1.csv`

## Figure group used here
- `nh_no_sensitivity`

## Run this sample
From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 samples/bar/sample_0008/plot.py
```

## Output path
```text
samples/bar/sample_0008/output.png
```

## Do not use this sample when
- when values are all positive and a grouped vertical bar chart is easier to read
- when the variable list is very short and horizontal layout is unnecessary

## Closest sibling samples
- `sample_0001`
- `sample_0009`

# sample_0004

## Reuse this sample when
- when the main figure has one dominant peak plus a low-magnitude region worth zooming
- when you need a secondary top axis
- when the same curves should appear in both the main plot and inset

## What pattern this script implements
This sample is a reusable template for a **single-panel line chart with inset zoom**.

## Data shape expected by this script
- several ordered line series over the same x-axis
- enough low-range detail for the inset region
- optional secondary-axis mapping handled in script

## How to adapt it
- replace the selected `figure_group` in `profile_series_v1.csv`
- update the inset x/y window in `plot.py`
- change the top-axis tick labels if your secondary axis represents another variable

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/profile_series_v1.csv`

## Figure group used here
- `heat_release_profiles`

## Run this sample
From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 samples/line/sample_0004/plot.py
```

## Output path
```text
samples/line/sample_0004/output.png
```

## Do not use this sample when
- when there is no meaningful region to zoom with an inset
- when the figure is primarily a scatter plot instead of smooth curves

## Closest sibling samples
- `sample_0005`
- `sample_0006`
- `sample_0013`

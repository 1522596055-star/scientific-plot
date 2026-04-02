# sample_0006

## Reuse this sample when
- when one variable is scanned continuously on the x-axis
- when multiple theory or model branches need to be compared
- when an unstable branch should be shown separately from the stable branch

## What pattern this script implements
This sample is a reusable template for a **parameter-scan curve plot with stable and unstable branches**.

## Data shape expected by this script
- ordered line series for each branch
- separate series for stable and unstable segments if they should look different
- a single shared x/y axis across all curves

## How to adapt it
- replace the series definitions in `profile_series_v1.csv` for your new parameter scan
- adjust color and linestyle mapping in `plot.py`
- update axis ranges and legend labels for the new physical variables

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/profile_series_v1.csv`

## Figure group used here
- `flame_coordinate_vs_flow`

## Run this sample
From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 samples/line/sample_0006/plot.py
```

## Output path
```text
samples/line/sample_0006/output.png
```

## Do not use this sample when
- when your figure is category-based rather than continuously scanned
- when the target does not have separate stable and unstable branches

## Closest sibling samples
- `sample_0004`
- `sample_0005`
- `sample_0013`

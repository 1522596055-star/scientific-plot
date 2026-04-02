# sample_0012

## Reuse this sample when
- when the y-axis spans orders of magnitude
- when comparing several fuels or formulations at the same x locations
- when points alone communicate the result better than fitted lines

## What pattern this script implements
This sample is a reusable template for a **log-scale ignition-delay scatter comparison**.

## Data shape expected by this script
- point-only series sharing one x-axis
- strictly positive y-values for the log axis
- multiple named series for comparison

## How to adapt it
- replace the series groups in `profile_series_v1.csv`
- keep the y-axis on log scale if your target also spans decades
- adjust markers and legend entries to match the compared formulations

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/profile_series_v1.csv`

## Figure group used here
- `ignition_delay_comparison`

## Run this sample
From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 samples/scatter/sample_0012/plot.py
```

## Output path
```text
samples/scatter/sample_0012/output.png
```

## Do not use this sample when
- when y-values can be zero or negative and a log axis is invalid
- when a fitted curve is more important than raw points

## Closest sibling samples
- `sample_0011`
- `sample_0019`

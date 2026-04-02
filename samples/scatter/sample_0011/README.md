# sample_0011

## Reuse this sample when
- when the same set of categories must be compared in two coordinate systems
- when only sparse points are needed and no connecting line is desired
- when marker shape/color encode material or method family

## What pattern this script implements
This sample is a reusable template for a **two-panel scientific scatter comparison**.

## Data shape expected by this script
- point-only rows with x and y values
- multiple named point groups
- optional separate panels for different derived metrics

## How to adapt it
- replace the scatter groups in `profile_series_v1.csv`
- update axis labels and units independently for the two panels
- adjust marker mapping if your classes differ

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/profile_series_v1.csv`

## Figure group used here
- `extinction_limits`

## Run this sample
From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 samples/scatter/sample_0011/plot.py
```

## Output path
```text
samples/scatter/sample_0011/output.png
```

## Do not use this sample when
- when your figure needs continuous connecting lines
- when point size is important and you really need a bubble plot

## Closest sibling samples
- `sample_0012`
- `sample_0019`

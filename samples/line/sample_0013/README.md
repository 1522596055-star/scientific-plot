# sample_0013

## Reuse this sample when
- when several rate conditions must be compared on one smooth curve plot
- when all curves share the same x variable and monotonic trend
- when the chart is primarily about curve shift rather than scatter

## What pattern this script implements
This sample is a reusable template for a **multi-line thermal decomposition or decay chart**.

## Data shape expected by this script
- several ordered line series on a common axis
- no point markers required unless the target figure needs them
- clearly named conditions for the legend

## How to adapt it
- replace the line series in `profile_series_v1.csv`
- update legend labels to match new rates or treatments
- adjust the x-range if your thermal or time window differs

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/profile_series_v1.csv`

## Figure group used here
- `polymer_mass_loss`

## Run this sample
From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 samples/line/sample_0013/plot.py
```

## Output path
```text
samples/line/sample_0013/output.png
```

## Do not use this sample when
- when you need an inset zoom or secondary axis
- when your curves contain many discrete observations with visible uncertainty bars

## Closest sibling samples
- `sample_0004`
- `sample_0005`
- `sample_0006`

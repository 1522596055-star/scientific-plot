# sample_0013

## Reuse this sample when
- when one x-axis and one y-axis are enough for the whole story
- when several simulation, model, or treatment curves should be overlaid cleanly
- when the figure is about curve shift or agreement rather than extra layout structure

## What pattern this script implements
This sample is a reusable template for a **plain multi-line scientific comparison chart**.

## Data shape expected by this script
- several ordered line series on one shared axis
- no point markers required unless the target figure truly needs them
- clearly named conditions or model variants for the legend

## How to adapt it
- replace the line series in `profile_series_v1.csv`
- update line styles and labels to match your methods or operating conditions
- adjust the x-range if your profile, time window, or coordinate span differs
- keep the plot single-axis unless a second axis is scientifically necessary

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/profile_series_v1.csv`

## Figure group used here
- `reduced_order_temperature_solutions`

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
- when a zoomed inset is needed to rescue a small region
- when branch structure or stable/unstable separation matters
- when repeated panels would be clearer than overlaying everything on one axis

## Closest sibling samples
- `sample_0004`
- `sample_0005`
- `sample_0006`

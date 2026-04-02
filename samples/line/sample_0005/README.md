# sample_0005

## Reuse this sample when
- when color should encode one variable and linestyle should encode another
- when several reactions or mechanisms must be overlaid on one axis
- when an early low-magnitude region also needs a zoomed inset

## What pattern this script implements
This sample is a reusable template for a **single-panel multi-line scientific profile with inset**.

## Data shape expected by this script
- multiple line series sharing the same x-axis
- series IDs that can be mapped into two visual dimensions
- optional inset-ready low-magnitude segment

## How to adapt it
- replace reaction/color and condition/linestyle mappings in `plot.py`
- reuse `profile_series_v1.csv` with one series per `(reaction, condition)` pair
- simplify or expand the two legends depending on the target figure

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/profile_series_v1.csv`

## Figure group used here
- `ch4_rate_profiles`

## Run this sample
From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 samples/line/sample_0005/plot.py
```

## Output path
```text
samples/line/sample_0005/output.png
```

## Do not use this sample when
- when one visual encoding is enough and you do not need both color and linestyle
- when the figure should be split into multiple panels instead of overlaying everything

## Closest sibling samples
- `sample_0004`
- `sample_0006`
- `sample_0013`

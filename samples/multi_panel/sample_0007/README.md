# sample_0007

## Reuse this sample when
- when two operating conditions should be compared side by side
- when each panel contains measured points with uncertainty and matching model lines
- when the same legend applies to both panels

## What pattern this script implements
This sample is a reusable template for a **two-panel measured-vs-modeled profile comparison**.

## Data shape expected by this script
- two or more panels with the same x-axis meaning
- point series that may include symmetric error bars
- paired line series representing modeled or fitted trends

## How to adapt it
- replace the panel IDs and titles in `plot.py`
- reuse `profile_series_v1.csv` with point and line series for each panel
- adjust shared y-range if your two panels differ more strongly

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/profile_series_v1.csv`

## Figure group used here
- `ells_profile_comparison`

## Run this sample
From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 samples/multi_panel/sample_0007/plot.py
```

## Output path
```text
samples/multi_panel/sample_0007/output.png
```

## Do not use this sample when
- when panel count is one and a single axis is enough
- when you do not need measured-vs-modeled pairing in each panel

## Closest sibling samples
- `sample_0002`
- `sample_0003`
- `sample_0010`
- `sample_0014`

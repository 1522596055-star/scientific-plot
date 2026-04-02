# sample_0010

## Reuse this sample when
- when several response variables share the same x-axis but not the same y-scale
- when two panels should be visually linked as part of one experimental story
- when line-plus-marker comparisons are more useful than bars

## What pattern this script implements
This sample is a reusable template for a **two-panel emissions comparison over a shared x-axis**.

## Data shape expected by this script
- one shared x variable across both panels
- multiple series per panel
- optional baseline series drawn as flat reference lines

## How to adapt it
- replace panel-specific series in `profile_series_v1.csv`
- reuse the same two-panel layout with custom y-axis labels
- adjust baseline reference lines if your target has control cases

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/profile_series_v1.csv`

## Figure group used here
- `engine_n_emissions`

## Run this sample
From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 samples/multi_panel/sample_0010/plot.py
```

## Output path
```text
samples/multi_panel/sample_0010/output.png
```

## Do not use this sample when
- when both metrics can share the same y-axis without confusion
- when bars communicate the comparison better than lines

## Closest sibling samples
- `sample_0002`
- `sample_0003`
- `sample_0007`
- `sample_0014`

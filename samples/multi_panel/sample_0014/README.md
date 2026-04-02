# sample_0014

## Reuse this sample when
- when two vertically stacked metrics share the same x-axis
- when the target publication shows one efficiency metric above another
- when two operating strategies must be compared consistently in both panels

## What pattern this script implements
This sample is a reusable template for a **stacked two-panel efficiency comparison over operating ratio**.

## Data shape expected by this script
- top-panel and bottom-panel line series
- same x variable for both panels
- one or more named comparison strategies

## How to adapt it
- replace the top and bottom panel series in `profile_series_v1.csv`
- reuse the stacked layout and shared x-axis
- update y-axis labels and limits separately for the two metrics

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/profile_series_v1.csv`

## Figure group used here
- `rcci_efficiency`

## Run this sample
From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 samples/multi_panel/sample_0014/plot.py
```

## Output path
```text
samples/multi_panel/sample_0014/output.png
```

## Do not use this sample when
- when your metrics should be overlaid on one axis instead of stacked
- when there are more than two or three comparison strategies and the panels become too dense

## Closest sibling samples
- `sample_0002`
- `sample_0003`
- `sample_0007`
- `sample_0010`

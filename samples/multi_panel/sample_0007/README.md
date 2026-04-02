# sample_0007

## Reuse this sample when
- when two validation quantities should be compared side by side
- when each panel contains reference markers plus one modeled line
- when one shared legend should explain both panels

## What pattern this script implements
This sample is a reusable template for a **two-panel validation pair**.

## Data shape expected by this script
- two panels with the same x-axis meaning
- one point series and one line series in each panel
- panel-specific y-labels and ranges

## How to adapt it
- replace the panel titles, labels, and ranges in `plot.py`
- reuse `profile_series_v1.csv` with one reference series and one modeled series per panel
- keep the legend shared unless the panels truly need different line/marker meanings

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/profile_series_v1.csv`

## Figure group used here
- `porous_media_validation_pair`

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
- when only one quantity matters and a single axis is enough
- when you need more than two repeated panels
- when the panel grammars differ too much to share one legend

## Closest sibling samples
- `sample_0002`
- `sample_0003`
- `sample_0010`
- `sample_0014`

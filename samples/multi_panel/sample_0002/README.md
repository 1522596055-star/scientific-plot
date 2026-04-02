# sample_0002

## Reuse this sample when
- when you need multiple aligned panels with similar axes
- when each panel combines model lines and experimental points
- when each panel shares the same visual grammar but different data series

## What pattern this script implements
This sample is a reusable template for a **three-panel line and marker comparison figure**.

## Data shape expected by this script
- panel-wise rows with `panel_id` and `series_id`
- line series stored as ordered x-y points
- point series stored as sparse x-y observations

## How to adapt it
- replace panel definitions and series order in `plot.py`
- reuse `profile_series_v1.csv` with a new `figure_group` and panel IDs
- adjust legend placement and axis ranges panel by panel

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/profile_series_v1.csv`

## Figure group used here
- `combustion_no_profiles`

## Run this sample
From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 samples/multi_panel/sample_0002/plot.py
```

## Output path
```text
samples/multi_panel/sample_0002/output.png
```

## Do not use this sample when
- when all content fits naturally on one axis
- when panel layouts are irregular or require nested subplots

## Closest sibling samples
- `sample_0003`
- `sample_0007`
- `sample_0010`
- `sample_0014`

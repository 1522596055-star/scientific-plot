# sample_0003

## Reuse this sample when
- when you need a grid of small multiples for different species or targets
- when each panel contains one smooth line and one error-bar point series
- when panel-specific axis limits differ slightly but the overall layout is shared

## What pattern this script implements
This sample is a reusable template for a **2x3 multi-panel experiment-vs-simulation figure**.

## Data shape expected by this script
- one `line` series and one `point` series per panel
- optional `error_low` and `error_high` for experimental observations
- panel-specific x/y limits defined in script or metadata

## How to adapt it
- replace the panel titles and limits in `plot.py`
- reuse `profile_series_v1.csv` with panel-specific `line` and `point` rows
- adjust error-bar styling if your target figure uses different markers

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/profile_series_v1.csv`

## Figure group used here
- `temperature_species_profiles`

## Run this sample
From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 samples/multi_panel/sample_0003/plot.py
```

## Output path
```text
samples/multi_panel/sample_0003/output.png
```

## Do not use this sample when
- when no error bars are needed
- when there is only one target variable and a single-panel figure is enough

## Closest sibling samples
- `sample_0002`
- `sample_0007`
- `sample_0010`
- `sample_0014`

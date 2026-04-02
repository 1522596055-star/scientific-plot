# sample_0002

## Reuse this sample when
- when you need several aligned validation panels with the same x-axis meaning
- when each panel repeats the same mean-vs-rms and simulation-vs-reference grammar
- when a compact 1x3 layout is clearer than either one overloaded axis or a denser 2x3 grid

## What pattern this script implements
This sample is a reusable template for a **three-panel repeated validation comparison**.

## Data shape expected by this script
- panel-wise rows with `panel_id` and repeated `series_id` values
- paired line series such as simulation mean and simulation rms
- paired point series such as reference mean and reference rms

## How to adapt it
- replace the panel definitions and series order in `plot.py`
- reuse `profile_series_v1.csv` with a new `figure_group` and aligned panel IDs
- keep the visual grammar stable across all panels
- only use this sample when the repeated-panel rhythm is the main structural idea

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/profile_series_v1.csv`

## Figure group used here
- `mixture_fraction_temperature_profiles`

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
- when only one panel is needed
- when each panel needs very different annotation, scales, or plotting grammar
- when the figure should really be a denser validation grid like `sample_0003`

## Closest sibling samples
- `sample_0003`
- `sample_0007`
- `sample_0010`
- `sample_0014`

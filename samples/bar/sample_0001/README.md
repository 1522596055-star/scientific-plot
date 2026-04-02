# sample_0001

## Reuse this sample when
- when you need two conditions compared across the same set of categories
- when each category has one aggregated value per condition
- when category-specific scale labels must be shown under the x-axis

## What pattern this script implements
This sample is a reusable template for a **grouped bar chart for categorical comparison**.

## Data shape expected by this script
- one row per `(condition_id, category_id)`
- a pre-aggregated `mean_value` for each bar
- optional scale information through `scale_power`

## How to adapt it
- replace the category order and labels in `plot.py`
- replace the condition IDs used from `categorical_measurements_v1.csv`
- update colors, axis label, and y-axis range

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/categorical_measurements_v1.csv`

## Figure group used here
- `combustion_intermediates`

## Run this sample
From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 samples/bar/sample_0001/plot.py
```

## Output path
```text
samples/bar/sample_0001/output.png
```

## Do not use this sample when
- when you need stacked bars instead of side-by-side bars
- when each category contains many raw observations and a distribution plot would be better

## Closest sibling samples
- `sample_0008`
- `sample_0009`

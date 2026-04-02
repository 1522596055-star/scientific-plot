# sample_0015

## Reuse this sample when
- when your data is naturally a matrix
- when row/column labels matter as much as the values
- when color plus inline numeric annotation is useful

## What pattern this script implements
This sample is a reusable template for a **correlation-style heatmap**.

## Data shape expected by this script
- one row per matrix cell
- explicit `row_id`, `col_id`, and numeric value
- a complete rectangular matrix

## How to adapt it
- replace row/column labels and values in `matrix_values_v1.csv`
- switch colormap and annotation formatting if needed
- adjust figure size based on matrix dimensions

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/matrix_values_v1.csv`

## Figure group used here
- `method_correlation_heatmap`

## Run this sample
From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 samples/heatmap/sample_0015/plot.py
```

## Output path
```text
samples/heatmap/sample_0015/output.png
```

## Do not use this sample when
- when your data is not naturally matrix-shaped
- when exact individual points matter more than grid structure

## Closest sibling samples
- None yet in this category.

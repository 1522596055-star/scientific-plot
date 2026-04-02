# data/shared

Reusable shared datasets for the plotting dataset.

Each dataset should have:
- one `.csv` file containing the values used by plotting scripts
- one `.metadata.json` file describing schema and intended figure groups

## Current shared datasets

- `categorical_measurements_v1.*` — grouped categorical values and sensitivity-bar style data
- `profile_series_v1.*` — line, scatter, multi-panel, inset, parameter-scan, reduced-order model-comparison, and validation-style profile figures
- `distribution_measurements_v1.*` — boxplot, violin, and histogram source values
- `matrix_values_v1.*` — heatmap-ready matrix data
- `scatter_points_v1.*` — clustered 2D scatter / bubble data

## Usage rule

When implementing a new sample:
1. check whether an existing dataset already contains a compatible figure group
2. if not, consider adding a new figure group to an existing dataset
3. only then create a brand-new dataset

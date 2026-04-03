# scientific-plotter test data

Synthetic datasets for testing the `scientific-plotter` skill.

## Files
- `catalyst_activity_summary.csv` — aggregated category comparison; good grouped-bar test
- `engine_dual_metric_scan.csv` — shared-x trend dataset with two response variables; good multi-panel line test
- `method_similarity_matrix.tsv` — labeled wide matrix; good annotated heatmap test
- `long_form_similarity_matrix.csv` — row/col/value matrix; good long-form heatmap test
- `treatment_conversion_repeats.csv` — repeated measurements by treatment; good boxplot test
- `ignition_delay_scan.csv` — positive response spanning a broad range; good log-scale scatter/line test
- `cluster_embedding_points.csv` — x/y/group/size data; good bubble-scatter test
- `validation_profile_with_errors.csv` — tidy panel/series/x/y/error table; should stay on a line/validation path rather than being misread as a heatmap

All files are synthetic and safe to use for experiments.

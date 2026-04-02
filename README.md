# scientific-plot

A reusable scientific plotting dataset and agent skill.

This repository now serves **two purposes**:
1. a reusable library of scientific plotting templates
2. a bundled `scientific-plotter` skill that agents can use to turn raw scientific data or vague plotting requests into publication-style figures

Each sample is a reproducible plotting unit with:
- a reference image or selected PDF figure when available
- a Python plotting script
- a rendered output image
- a sample README for humans and agents
- metadata describing the data source and chart type

The repository is organized to help an agent quickly answer four questions:
1. **What chart families already exist?**
2. **What shared datasets should be reused first?**
3. **Where did a sample come from: image, PDF, or internal coverage expansion?**
4. **How can this repository be used directly as an agent skill on any machine?**

## Repository layout

```text
scientific-plot/
  README.md
  requirements.txt
  data/
    README.md
    shared/
      README.md
      *.csv
      *.metadata.json
  pdf/
    README.md
    *.pdf
  ref/
    README.md
    image_selected/
    pdf_selected/
  samples/
    README.md
    bar/
    line/
    multi_panel/
    scatter/
    distribution/
    heatmap/
  skills/
    scientific-plotter/
      SKILL.md
      scripts/
      references/
      evals/
  test-data/
    README.md
    *.csv
    *.tsv
```

## Main directories

### `data/shared/`
Reusable synthetic datasets.

These are the first place to look before creating any new data.
Each dataset has:
- one `.csv`
- one `.metadata.json`

### `pdf/`
Archived source papers with normalized filenames.

These are preserved as sources for figure selection. We usually choose **at most one figure per PDF**, and only when the figure has good reuse value.

### `ref/`
Reference figures already selected for the dataset.

Subfolders:
- `ref/image_selected/` — references that came from standalone images
- `ref/pdf_selected/` — references cropped or selected from archived PDFs

### `samples/`
Finished plotting samples grouped by chart family.

Each sample directory contains:
- `plot.py`
- `output.png`
- `meta.json`
- `README.md`

### `skills/scientific-plotter/`
A bundled Agent Skills-compatible skill.

This skill can:
- read raw CSV/TSV/XLSX data
- infer a likely chart family when the user does not know what chart to use
- search the local sample library for the closest structural template
- generate a standalone `plot.py`
- render the final `output.png`

### `test-data/`
Synthetic datasets for smoke testing the skill on any machine.

## Sample categories

- `samples/bar/` — grouped bars and horizontal sensitivity bars
- `samples/line/` — single-panel lines, inset curves, parameter scans
- `samples/multi_panel/` — 2-panel, 3-panel, or grid-based figures
- `samples/scatter/` — scatter, sparse scientific point plots, log-scatter, bubble scatter
- `samples/distribution/` — boxplot, violin, histogram
- `samples/heatmap/` — matrix heatmaps

## Use this repository as an agent skill

This repository follows the Agent Skills layout by placing the skill in:

```text
skills/scientific-plotter/
```

Because the skill uses **repository-relative paths**, it is portable across machines after cloning.

### Pi installation

Clone the repository, then add its `skills/` directory to your global Pi settings:

```json
{
  "skills": [
    "/path/to/scientific-plot/skills"
  ]
}
```

After restarting Pi or opening a new session, the `scientific-plotter` skill should be discoverable.

### Other agent harnesses

Any harness that supports the Agent Skills directory layout can point at:

```text
<repo>/skills/
```

or directly at:

```text
<repo>/skills/scientific-plotter/
```

## Test datasets

Ready-made test files are in `test-data/`:
- `catalyst_activity_summary.csv` — grouped bar candidate
- `engine_dual_metric_scan.csv` — shared-x multi-panel line candidate
- `method_similarity_matrix.tsv` — annotated heatmap candidate
- `treatment_conversion_repeats.csv` — boxplot candidate
- `ignition_delay_scan.csv` — log-scale scatter/line candidate
- `cluster_embedding_points.csv` — bubble-scatter candidate

## Workflow conventions

### When a new image is added
1. Move it into `ref/image_selected/` with a normalized filename.
2. Reuse an existing shared dataset if possible.
3. Create or update one sample.

### When a new PDF is added
1. Move it into `pdf/` with a normalized filename.
2. Inspect figures in the paper.
3. Choose **one** figure with the highest reuse value.
4. Save the chosen figure into `ref/pdf_selected/`.
5. Reuse existing shared datasets when possible.

### When adding new data
Prefer this order:
1. reuse an existing shared dataset
2. extend an existing shared dataset with a new figure group
3. create a new shared dataset only if the chart type really needs it

## Run a sample
From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 samples/<category>/<sample_id>/plot.py
```

Example:

```bash
python3 samples/bar/sample_0001/plot.py
```

## Notes for future agents
- Prefer reuse over proliferation.
- Keep reference handling simple and traceable.
- Keep sample READMEs operational: what it does, what data it uses, how to run it.
- Do not add many near-duplicate figures from the same paper.
- Prefer structure matching over domain-word matching when choosing a plotting template.

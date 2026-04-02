# scientific-plot

A reusable scientific plotting dataset and agent skill.

This repository now serves **three linked purposes**:
1. a reusable library of scientific plotting templates
2. a bundled `scientific-plotter` skill that turns raw scientific data or vague plotting requests into publication-style figures
3. a distilled knowledge layer that captures strong paper-figure ideas without forcing every idea into a new script template

Each sample is a reproducible plotting unit with:
- a reference image or selected PDF figure when available
- a Python plotting script
- a rendered output image
- a sample README for humans and agents
- metadata describing the data source and chart type

The repository is organized to help an agent quickly answer six questions:
1. **What chart families already exist?**
2. **What shared datasets should be reused first?**
3. **Which templates are canonical starters vs narrow variants?**
4. **What good paper-figure ideas should be reused even when they do not deserve a full new sample?**
5. **How should simulation-heavy papers influence curation without creating too many extra samples?**
6. **How can this repository be used directly as an agent skill on any machine?**

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
    CURATED_INSIGHTS.md
    SIMULATION_CURATION.md
    *.pdf
    inbox/
  ref/
    README.md
    image_selected/
    pdf_selected/
  patterns/
    README.md
    line.md
    multi_panel.md
    composite.md
    numerical_simulation.md
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
Archived source papers plus an inbox for untriaged downloads.

- normalized, curated PDFs stay directly under `pdf/`
- `pdf/CURATED_INSIGHTS.md` captures soft takeaways from the already curated archive
- `pdf/SIMULATION_CURATION.md` is the full-review map for simulation-heavy papers
- new downloads should move to `pdf/inbox/` immediately so the repository root stays clean
- not every new PDF should become a sample

### `ref/`
Reference figures already selected for the dataset.

Subfolders:
- `ref/image_selected/` — references that came from standalone images
- `ref/pdf_selected/` — references cropped or selected from archived PDFs

### `patterns/`
Distilled plotting judgment.

This is the key layer for ideas that are worth keeping but do **not** justify another `plot.py` template.
Use it to preserve published-paper wisdom without overwhelming agents with too many similar references.

Current notes include:
- `line.md`
- `multi_panel.md`
- `composite.md`
- `numerical_simulation.md`

### `samples/`
Finished plotting samples grouped by chart family.

Each sample directory contains:
- `plot.py`
- `output.png`
- `meta.json`
- `README.md`

The busiest categories should stay intentionally small and curated.
For now, `line/` and `multi_panel/` are explicitly split into canonical starters and narrower variants.

### `skills/scientific-plotter/`
A bundled Agent Skills-compatible skill.

This skill can:
- read raw CSV/TSV/XLSX data
- infer a likely chart family when the user does not know what chart to use
- read distilled pattern notes to avoid overreacting to raw references
- search the local sample library for the closest structural template
- generate a standalone `plot.py`
- render the final `output.png`

### `test-data/`
Synthetic datasets for smoke testing the skill on any machine.

## Retrieval philosophy

The repository is intentionally layered.
An agent should usually work in this order:
1. understand the data and task
2. read `patterns/` for the relevant family if available
3. if the task is simulation-heavy, also read `patterns/numerical_simulation.md`
4. if the task involves sample refresh or PDF curation, read `pdf/SIMULATION_CURATION.md`
5. choose a **canonical** starter sample
6. only then open variant samples
7. only consult raw references or PDFs if the distilled layers are still insufficient

This keeps the agent from being buried in too many reference images while still preserving paper-quality design judgment.

## Sample categories

- `samples/bar/` — grouped bars and horizontal sensitivity bars
- `samples/line/` — curated single-panel lines, inset curves, parameter scans
- `samples/multi_panel/` — curated 2-panel, 3-panel, or grid-based figures
- `samples/scatter/` — scatter, sparse scientific point plots, log-scatter, bubble scatter
- `samples/distribution/` — boxplot, violin plots, histograms
- `samples/heatmap/` — matrix heatmaps

## Use this repository as an agent skill

This repository follows the Agent Skills layout by placing the skill in:

```text
skills/scientific-plotter/
```

Because the skill uses repository-relative paths, it is portable across machines after cloning.

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
1. move it into `ref/image_selected/` with a normalized filename
2. reuse an existing shared dataset if possible
3. either create/update one sample or distill the idea into `patterns/`

### When a new PDF is added
1. move it into `pdf/inbox/` immediately so the repository root stays clean
2. inspect the paper
3. decide whether it should become:
   - a canonical sample
   - a secondary variant sample
   - a distilled note in `patterns/`
   - or an archive-only PDF with no promotion
4. if the paper is simulation-heavy, also update the simulation curation docs before deciding on a promotion
5. if promoted, normalize filenames and update the relevant README mappings

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
- Prefer `patterns/` over raw references when the family already has distilled guidance.
- Give newer simulation-relevant papers extra weight when they overlap with older samples.
- Use `pdf/SIMULATION_CURATION.md` when simulation-heavy papers start to dominate the curation question.
- Treat `pdf/inbox/` as a triage queue, not as a sample backlog.
- Keep canonical samples few and high-value.
- Keep sample READMEs operational: what it does, what data it uses, how to run it.
- Do not add many near-duplicate figures from the same paper.
- Prefer structure matching over domain-word matching when choosing a plotting template.

# scientific-plot

A reusable scientific plotting library with a bundled agent skill.

This repository is designed to be **small in templates, rich in judgment, and tidy in references**.
It is not a paper gallery. It is a working library for turning real scientific data into figures that feel calm, legible, and publication-minded.

## What lives here

The repository has four deliberate layers:

1. **`samples/`** — a compact set of reusable plotting templates
2. **`reference-samples/`** — curated paper figures that are useful but not honestly reproducible as templates
3. **`patterns/`** — distilled visual judgment that should not become another sample
4. **`ref/`** — the broader reference system: source papers, selected figures, inbox material, and curation notes

That split matters.
The aim is to keep code retrieval fast while still preserving what the papers taught us.

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
  ref/
    README.md
    figures/
      README.md
      selected/
    papers/
      README.md
      INSIGHTS.md
      SIMULATION.md
      archive/
      inbox/
        README.md
        TRIAGE.md
        PRIORITY.md
  patterns/
    README.md
    line.md
    multi_panel.md
    composite.md
    numerical_simulation.md
  reference-samples/
    README.md
    line/
    multi_panel/
    composite/
  samples/
    README.md
    REFRESH_CANDIDATES.md
    bar/
    line/
    multi_panel/
    scatter/
    distribution/
    heatmap/
  skills/
    scientific-plotter/
  test-data/
```

## How to navigate the repository

### `samples/`
Start here when you need actual plotting code.
Each sample is a complete reusable unit with:
- `plot.py`
- `output.png`
- `meta.json`
- `README.md`

The busy families are intentionally curated into **canonical starters** and **variants**.
Agents should begin with the canonical starters.

### `patterns/`
Read these before opening many samples.
These notes hold the quiet decisions that papers repeatedly reinforced:
- when a figure should stay single-panel
- when a grid is justified
- when a field view belongs with profile cuts
- when simulation plots are really trust-building validation figures rather than generic line charts

### `reference-samples/`
This is the curated non-reproducible layer.
Use it for paper figures that are worth opening during real work, even though the repository cannot honestly rebuild them as executable templates.
Each reference-only sample contains:
- `reference.png`
- `meta.json`
- `README.md`

### `ref/`
This is the broader reference system.
Both papers and selected figures live here because they are the same kind of evidence.

- `ref/figures/selected/` — the image references tied to samples
- `ref/papers/archive/` — normalized papers already absorbed into the library
- `ref/papers/inbox/` — normalized papers still under review
- `ref/papers/INSIGHTS.md` — what the curated papers taught us
- `ref/papers/SIMULATION.md` — the fuller simulation-heavy curation map

There is intentionally **no separate top-level PDF area** anymore.
Papers and cropped figures belong to one reference layer.

## Retrieval order for agents

A good default order is:

1. understand the user’s data and goal
2. read the relevant note in `patterns/`
3. if the task is simulation-heavy, also read:
   - `patterns/numerical_simulation.md`
   - `ref/papers/SIMULATION.md`
4. choose a canonical starter in `samples/`
5. only then open variant samples if a specific executable detail is truly needed
6. if the executable layer is still insufficient, consult `reference-samples/`
7. browse the broader `ref/` archive only as a final fallback

This keeps agents from getting buried in papers while still preserving paper-grade judgment.

## Sample families

- `samples/bar/` — grouped bars and horizontal sensitivity summaries
- `samples/line/` — plain line starters, inset lines, parameter scans
- `samples/multi_panel/` — stacked metrics, validation pairs, dense grids
- `samples/scatter/` — sparse scientific point comparisons, log scatter, bubble scatter
- `samples/distribution/` — boxplot, violin, histogram
- `samples/heatmap/` — matrix heatmaps

## Reference workflow

### When a new image arrives
1. move it into `ref/figures/selected/` with a normalized filename
2. reuse an existing shared dataset if possible
3. either update one sample, preserve it in `reference-samples/`, or distill the idea into `patterns/`

### When a new paper arrives
1. move it into `ref/papers/inbox/`
2. rename it immediately into a readable normalized filename
3. record the original download name in the inbox README mapping
4. decide whether its best home is:
   - a refreshed sample
   - a new variant sample
   - a reference-only sample
   - a pattern note
   - or retained archive-only evidence
5. if it is absorbed, move it to `ref/papers/archive/` and update the curation notes

## Shared data policy

Prefer this order:
1. reuse an existing shared dataset
2. extend an existing shared dataset with a new figure group
3. create a new shared dataset only when the structure truly requires it

## Use as an agent skill

The bundled skill lives in:

```text
skills/scientific-plotter/
```

Add the repository’s `skills/` directory to Pi settings:

```json
{
  "skills": [
    "/path/to/scientific-plot/skills"
  ]
}
```

Then the `scientific-plotter` skill can be loaded on demand or triggered automatically for plotting tasks.

## Practical stance

This repository should feel:
- selective rather than exhaustive
- elegant rather than crowded
- structurally reusable rather than paper-specific
- especially friendly to simulation-heavy validation work without becoming a simulation-paper scrapbook

# patterns

Distilled plotting ideas that sit between raw paper references and fully reproducible samples.

Use this directory when you want the **good scientific judgment** from published figures without drowning an agent in too many near-duplicate examples.

## Why this layer exists

Not every useful paper figure should become a new `plot.py` template.

A figure may be worth keeping because it teaches:
- when to split one figure into multiple panels
- when to add an inset
- how to encode two variables with color and linestyle
- how to place legends and annotations lightly
- how to simplify a paper figure into a reusable plotting pattern

Those lessons belong here even when the exact figure is too domain-specific or too detailed to justify a new sample.

## Three-layer curation model

### 1. Canonical samples
Keep a **small** set of starter templates in `samples/`.
These are the first place an agent should look for reusable plotting code.

### 2. Pattern notes
Use `patterns/` for ideas that are valuable but do not need a dedicated script template.
This is the main place to capture visual judgment from papers.

### 3. Raw references
Keep original images and PDFs in `ref/` and `pdf/`, but do not make them the default retrieval surface.
They are evidence and fallback material, not the first thing an agent should browse.

## Current focus

The repository currently needs the most distillation in the busiest or highest-context families:
- `line.md`
- `multi_panel.md`
- `composite.md`
- `numerical_simulation.md`

For a full-review map of simulation-oriented papers across both the archive and the inbox, also see:
- `../pdf/SIMULATION_CURATION.md`

## How an agent should use this directory

1. choose the chart family from the data and user goal
2. read the matching pattern note if it exists
3. if the task is simulation-heavy, also read `numerical_simulation.md`
4. start from the canonical starter sample for that family
5. only open variant samples if a specific feature is required
6. only fall back to raw references if the pattern note and samples are still insufficient

## Promotion rules for new papers

When a new paper or figure arrives, decide which bucket it currently seems to fit best:
- **canonical sample** — promote only if it adds a broadly reusable structure
- **variant sample** — keep only if it adds one important reusable feature without becoming a main starter
- **pattern note** — summarize the idea here if the value is mostly conceptual
- **archive only** — keep the PDF/reference without promoting it if it adds little retrieval value

For already curated papers, see `../pdf/CURATED_INSIGHTS.md`.
For simulation-heavy curation, see `../pdf/SIMULATION_CURATION.md`.
For newly downloaded papers, see:
- `../pdf/inbox/TRIAGE.md`
- `../pdf/inbox/NUMERICAL_PRIORITY.md`

For existing templates most likely to be refreshed by newer simulation papers, see `../samples/REFRESH_CANDIDATES.md`.

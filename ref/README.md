# ref

The repository’s unified reference layer.

Papers and selected figures live together here because they serve the same purpose:
**they are evidence for how a plotting template or pattern note was chosen.**

## Structure

- `figures/selected/` — reference images tied to individual samples
- `papers/archive/` — normalized papers already absorbed into the library
- `papers/inbox/` — normalized papers still under review
- `papers/INSIGHTS.md` — soft takeaways from the archived papers
- `papers/SIMULATION.md` — the fuller simulation-heavy curation map

## Design rule

Do not split references into separate top-level systems for “images” and “PDFs”.
Keep them together here, with clean subfolders and clean naming.

## Naming rule

- figures stay tied to the sample that uses them, e.g. `sample_0003_flamelet_validation_grid.jpg`
- papers use readable normalized filenames, not raw download IDs

## Retrieval rule

Agents should not browse this layer first.
They should usually start with:
1. `patterns/`
2. `samples/`
3. executable variants where relevant
4. `reference-samples/` when a non-reproducible paper figure is still useful
5. then `ref/` only if needed

# samples

Finished plotting samples, organized by chart family.

This directory is intentionally grouped by **visual form** rather than by paper source, because an agent usually retrieves reusable plotting templates more effectively by chart family first.

## How to use this directory

A practical search strategy is:
1. choose the chart family that matches the target figure structure
2. if a matching note exists under `../patterns/`, read it first
3. if the task is simulation-heavy, also read `../patterns/numerical_simulation.md`
4. open the category README
5. start from the category's **canonical starter template**
6. only open variant samples if a specific feature is required
7. adapt the closest sample-level README and script

## Canonical starters vs variants

Not every sample should be treated equally.

- **canonical starters** are the main reusable templates an agent should try first
- **variants** are useful, but should only be opened when their distinguishing feature is actually needed

This distinction matters most in crowded families such as `line/` and `multi_panel/`.

## Category overview

- `bar/` — grouped bars and horizontal bar-style sensitivity charts
- `line/` — curated single-panel line starters plus a few dense variants
- `multi_panel/` — curated multi-panel starters plus a few structural variants
- `scatter/` — sparse point plots, scatter charts, log-scatter charts, bubble scatter
- `distribution/` — boxplots, violin plots, histograms
- `heatmap/` — matrix-valued heatmaps

## Pattern notes

Use these distilled notes before diving into too many raw references:
- `../patterns/line.md`
- `../patterns/multi_panel.md`
- `../patterns/composite.md` when chart+image/schematic/field-map structure is involved
- `../patterns/numerical_simulation.md` when simulation-heavy judgment matters

For a repository-wide map of current simulation-heavy papers, see:
- `../pdf/SIMULATION_CURATION.md`

## When to search each category first

- search `bar/` first when the target figure compares discrete categories
- search `line/` first when one axis with continuous x-values is enough
- search `multi_panel/` first when the figure is naturally split into repeated subplots
- search `scatter/` first when individual observations matter more than smooth curves
- search `distribution/` first when raw value distributions are the main message
- search `heatmap/` first when the data is naturally a matrix

## Sample contract

Every sample directory should contain:
- `plot.py` — the executable plotting script
- `output.png` — the rendered result
- `meta.json` — machine-readable metadata
- `README.md` — reuse-oriented instructions for humans and agents

## Path pattern

```text
samples/<category>/<sample_id>/
```

Example:

```text
samples/bar/sample_0001/
samples/multi_panel/sample_0003/
samples/heatmap/sample_0015/
```

# samples

Finished plotting samples, organized by chart family.

This directory is intentionally grouped by **visual form** rather than by paper source, because an agent usually retrieves reusable plotting templates more effectively by chart family first.

## How to use this directory

A practical search strategy is:
1. choose the chart family that matches the target figure structure
2. open that category README
3. start from the recommended starter sample
4. adapt the closest sample-level README and script

## Category overview

- `bar/` — grouped bars and horizontal bar-style sensitivity charts
- `line/` — single-panel line charts, inset curves, and continuous parameter scans
- `multi_panel/` — figures with multiple aligned subplots
- `scatter/` — sparse point plots, scatter charts, log-scatter charts, bubble scatter
- `distribution/` — boxplots, violin plots, histograms
- `heatmap/` — matrix-valued heatmaps

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

# samples

Finished plotting templates, organized by chart family.

This directory is grouped by **visual form**, not by source paper.
That keeps retrieval practical: agents usually find the right template faster by structure than by domain topic.

## How to use this directory

A good working order is:
1. identify the target figure family
2. read the matching note in `../patterns/`
3. if the task is simulation-heavy, also read:
   - `../patterns/numerical_simulation.md`
   - `../ref/papers/SIMULATION.md`
4. open the relevant category README
5. start from the family’s **canonical starter**
6. only open variants when a specific structural detail is truly needed
7. if the executable layer is still too simple, consult `../reference-samples/`

## Canonical starters and variants

Not every sample should be treated equally.

- **canonical starters** are the default templates an agent should try first
- **variants** are narrower and should only be opened when their distinguishing feature is clearly relevant

This matters most in the line and multi-panel families.

## Category overview

- `bar/` — grouped bars and horizontal sensitivity summaries
- `line/` — single-panel lines, inset lines, parameter scans
- `multi_panel/` — validation pairs, compact repeats, dense grids, stacked metrics
- `scatter/` — sparse point comparisons, log scatter, bubble scatter
- `distribution/` — boxplot, violin, histogram
- `heatmap/` — matrix heatmaps

## Pattern notes to read first

- `../patterns/line.md`
- `../patterns/multi_panel.md`
- `../patterns/composite.md` when chart+image / field-map structure matters
- `../patterns/numerical_simulation.md` when the figure is validation-heavy or simulation-oriented

## Sample contract

Every sample directory should contain:
- `plot.py`
- `output.png`
- `meta.json`
- `README.md`

## Path pattern

```text
samples/<category>/<sample_id>/
```

Examples:

```text
samples/line/sample_0013/
samples/multi_panel/sample_0003/
samples/heatmap/sample_0015/
```

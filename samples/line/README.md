# line

Single-panel line-oriented samples.

This category is intentionally curated into a **small set of canonical starters** plus one denser variant, so agents do not have to browse many near-duplicate line figures.

## What belongs here
- ordinary line charts
- inset line charts
- parameter-scan curves
- single-axis multi-line comparisons

## Read this before browsing too many samples
- `../../patterns/line.md`

## When to search this category first
- when one main axis is enough for the figure
- when trends over a continuous x variable are the main story
- when several curves must be overlaid in one panel
- when an inset zoom is needed without converting to a multi-panel figure

## Canonical starter templates
- `sample_0013` — primary starter for ordinary multi-line scientific trends and model-comparison profiles
- `sample_0004` — primary starter for line charts with inset zoom and optional secondary top axis
- `sample_0006` — primary starter for parameter scans and branch-separated curves

## Secondary variant
- `sample_0005` — dense dual-encoding overlay (use only when both color and linestyle carry essential meaning)

## How to choose within this category
- start with `sample_0013` for most plain multi-line plots
- switch to `sample_0004` when a scientifically important local region needs a zoomed inset
- switch to `sample_0006` when branch structure or stable/unstable behavior matters
- only use `sample_0005` when one visual encoding is not enough

## When to avoid this category
- when the target figure is mostly categorical and should use bars
- when the layout requires multiple coordinated subplots
- when the figure is mainly about point clouds or distributions

## Samples
- `sample_0013` — plain multi-line model / trend comparison `[canonical]`
- `sample_0004` — line chart with inset and secondary top axis `[canonical]`
- `sample_0006` — parameter-scan curve plot with branch separation `[canonical]`
- `sample_0005` — dense overlay with color + linestyle encoding `[variant]`

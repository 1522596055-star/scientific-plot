# Selection rubric

Use this rubric when several samples look plausible.

## Prefer structural match over topic match

A sample about combustion may still be the right template for biology, materials, or economics if the chart structure is the same.

Rank candidates by:
1. same chart family
2. same panel layout
3. same visual encodings
4. same axis behavior
5. same overall visual density
6. same domain only as a final tiebreaker

## Family cues

### Bar
Choose bar samples when values are already aggregated by category.
Look for grouped bars or horizontal signed bars.

### Line
Choose line samples when the x-axis is continuous and the main story is a trend or profile.
Inset figures belong here unless the figure is truly multi-panel.

### Multi-panel
Choose multi-panel samples when one figure contains repeated coordinated subplots.
Prefer this family over single-panel line charts when the reader should compare panels side by side.

### Scatter
Choose scatter samples when individual points matter more than connecting curves.
Use bubble scatter only when marker size carries meaning.

### Distribution
Choose distribution samples when raw observations are the main input.
Use boxplots for quartiles, violins for shape, histograms for one-variable frequency.

### Heatmap
Choose heatmap samples when data is fundamentally a matrix.
Do not force independent observations into a heatmap.

## Prefer canonical starters before variants

In crowded families such as `line` and `multi_panel`, read the repository's pattern notes and category README first.
Start from a sample whose `meta.json` marks it as `canonical` unless the distinguishing feature of a variant is explicitly needed.

## Combining templates

Use one primary sample whenever possible.
Borrow from a second sample only for a clearly isolated feature such as:
- inset handling
- error bars
- legend treatment
- log-axis behavior

If you find yourself borrowing from three or more samples, step back and simplify.

## Standalone output rule

The final user-facing `plot.py` should be self-contained.
Do not leave the script pointing at repository-internal data paths unless the user explicitly asked to work inside this repository.

## Scientific style rule

Aim for figures that feel like a paper figure:
- restrained color palette
- readable labels
- adequate whitespace
- no gratuitous effects
- legends only when they add meaning

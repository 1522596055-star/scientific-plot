# composite patterns

Distilled guidance for figures that mix charts with images, schematics, parameter maps, or field reconstructions.

These ideas are often excellent in published papers, but they usually should **not** become the default plotting template for ordinary user data.
Use them selectively when the scientific story genuinely requires more than a plain chart.
These are best read as prompts for judgment, not as mandatory triggers.

## When this pattern family is useful

Use composite thinking when the figure needs to communicate one of these:
- a transient event with visually distinct stages
- a strong connection between instrumentation/setup and measured data
- a regime map or response surface over two control variables
- a side-by-side comparison of reconstructed fields or image-like scientific outputs
- a review-style summary where the point is conceptual synthesis rather than one dataset alone
- a simulation figure where spatial structure and quantitative cuts need to reinforce each other

## High-value ideas distilled from the current PDF set

### 1. Time-series plus synchronized image strip
Seen in papers on battery-fire emissions, fire HRR prediction, and plasma-assisted scramjet stabilization.

Use when:
- the timing of events matters
- the visual state of the system changes sharply over time
- a line chart alone would hide what happened physically at key moments

Good structure:
- top row: a few representative frames or snapshots
- bottom row: one or two aligned time-series axes with event markers

Do not use by default when the user only has tabular trend data and no meaningful image snapshots.

### 2. Experimental schematic plus one main data panel
Seen in co-firing, plasma, and diagnostics papers.

Use when:
- geometry or measurement placement is essential to interpret the result
- the user is presenting a method, setup, or apparatus alongside data

Good rule:
- the schematic should support interpretation, not dominate the page
- for reusable templates, keep the idea but simplify the artwork burden

### 3. Parameter map / regime map
Seen in thermoacoustic review figures and some combustion stability papers.

Use when:
- the user has two control variables and one response quantity
- the main point is non-monotonic behavior or regime boundaries
- a family of many line plots would be harder to read than a 2D map

Good outputs may be:
- heatmap
- contour map
- scatter-with-color map

This is a strong candidate for future expansion of the repository, but it should be promoted carefully because it is structurally different from the current line-heavy set.

### 4. Side-by-side field comparison
Seen in reacting-flow PINN papers and image-based diagnostics.

Use when:
- the user wants to compare prediction vs reference, before vs after, or experiment vs reconstruction
- the data is spatial or image-like rather than a simple x-y table

Good structure:
- left/right field maps with identical color scales
- optional profile cuts underneath or at the side

This should not be forced into ordinary line or scatter templates.

### 5. Review-style concept + comparison hybrids
Seen in sustainable-combustion and biomass-pyrolysis review papers.

Use when:
- the figure is summarizing a landscape of options, pathways, or tradeoffs
- the user needs an explanatory artifact rather than only one measurement plot

Examples of reusable ideas:
- energy density comparison maps
- process-chain schematics
- product-distribution summary charts

For the current repository, these usually belong in `patterns/` rather than as new samples unless the structure becomes repeatedly useful.

### 6. Field snapshot plus profile cuts
Seen in spray LES, ammonia-flame LES, porous-media validation, and dual-fuel swirl DNS papers.

Use when:
- the figure needs one or more contours to show spatial structure
- but the scientific claim still depends on centerline, radial, or conditional profiles
- the chart should help the reader trust the field view rather than replace it

Good structure:
- field / contour panel for context
- aligned profile or cut panels for quantification
- matching labels or sampling locations so the relationship is explicit

This is one of the most important composite ideas for simulation-heavy work.

### 7. Accuracy / cost / solver-comparison composites
Seen in reduced-order chemistry, ML-for-LES, and quantum-computing papers.

Use when:
- the story is partly about predictive agreement and partly about computational cost or model complexity
- one chart alone cannot communicate both accuracy and efficiency tradeoffs

Good structure:
- left: prediction or profile comparison
- right or lower panel: cost, timesteps, error, or complexity summary

Do **not** copy the full paper structure into a sample unless this tradeoff view becomes a repeated user need.

### 8. Uncertainty propagation and sensitivity decomposition
Seen in surrogate-model and uncertainty papers.

Use when:
- the user wants to show uncertainty bands, parity, and parameter importance together
- one panel alone would hide either the validation quality or the source of uncertainty

Good outputs may mix:
- parity plots
- profile uncertainty bands
- Sobol-style importance summaries

At the moment, this is better treated as pattern-level guidance than as a default template.

## What not to do

- do not turn every good paper composite into a new plotting template
- do not mix schematics and data just because the paper did so
- do not create image-strip panels when no meaningful event imagery exists
- do not let conceptual diagrams replace a clean quantitative chart when the user's task is primarily data presentation
- do not promote a simulation paper into `samples/` if its main value is really the combination of many heterogeneous panels

## Current triage recommendation

Most figures from `pdf/inbox/` that fall into this family should be treated as:
- **pattern-only inspirations** first
- **future sample candidates** only if the same composite structure keeps appearing across tasks

For the current full-review map of simulation-heavy papers, also see:
- `../pdf/SIMULATION_CURATION.md`

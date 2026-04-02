# numerical simulation patterns

Soft guidance distilled from papers that are especially relevant to simulation-heavy combustion workflows.

This note exists because a repository can be visually clean yet still drift away from the figures a numerical-simulation group actually needs.
The repository has now been re-centered using a fuller simulation review, so this note should be read together with:
- `../pdf/SIMULATION_CURATION.md`

## What this note is for

Use this note when the task sounds like:
- LES / DNS / RANS / flamelet / DCMC / reduced-order modeling
- simulation vs experiment comparison
- centerline or radial profile validation
- conditional mean / rms profile comparison
- contour field plus reduced profile summaries
- transient flame evolution in simulation time

These are not rigid rules. They are recurring patterns that seem particularly valuable for a simulation-oriented group.

## High-value tendencies from the current simulation set

### 1. Many simulation plots are really trust-building validation views
In simulation papers, line and panel figures often appear as:
- centerline profiles
- radial cuts at fixed heights
- temperature / species / HRR / OH comparisons
- simulation vs experiment overlays
- reduced-order model vs detailed chemistry comparisons

The visual goal is often **credibility** rather than only trend display.
That usually means:
- cleaner legends
- explicit normalization (`x/d`, `z/D`, `u/u_CJ`, `ξ`, etc.)
- direct overlays of reference and prediction
- fewer decorative choices

### 2. Mean and fluctuation can both matter
Several simulation papers pair:
- mean value
- rms / fluctuation / spread

That does not automatically require a new chart family, but it is a reminder that a validation figure may need more than one curve or one panel to feel scientifically complete.

### 3. Field structure and profile cuts often belong together
Some of the strongest simulation papers combine:
- contour or pseudocolor fields
- one or more profile cuts or conditional profiles

This is often a better mental model than trying to decide between “only fields” and “only lines.”
When a user task sounds spatial and validation-heavy, read `composite.md` too.

### 4. Accuracy / complexity figures are often pattern-level, not sample-level
Many simulation papers include:
- parity or error views
- timestep or CPU-time comparisons
- solver or closure-model complexity summaries

These are valuable scientifically, but they do **not** always deserve another plotting starter.
Usually the right move is to preserve the judgment in `patterns/` and keep `samples/` small.

### 5. Simulation papers split into a few recurring reusable structures
Across the current curated and inbox set, the main reusable structures are still relatively few:
- plain multi-line model comparison
- compact repeated validation panels
- dense validation grids
- two-panel validation pairs
- parameter scans with branch behavior
- field + profile composites

This is why the repository should refresh anchors selectively rather than keep adding more samples.

## Current simulation-aligned anchors in the repository

### `sample_0013` — plain multi-line trend/profile
Refreshed with:
- `local_principal_component_transport_reacting_flow.pdf`

Why this refresh made sense:
- it preserved the clean single-axis multi-line structure
- it shifted the canonical line starter toward reduced-order reacting-flow comparisons that are closer to downstream simulation usage
- it stayed simpler than a dual-axis or multi-panel alternative

### `sample_0002` — compact repeated profile comparison
Refreshed with:
- `large_eddy_simulation_partially_cracked_ammonia_flames.pdf`

Why this refresh made sense:
- the source paper offered repeated validation panels with the same grammar across locations
- it improved topical relevance without collapsing into a denser grid already covered by `sample_0003`

### `sample_0003` — dense multi-panel grid
Refreshed with:
- `four_fuel_stream_flamelet_pulverized_coal_ammonia_combustion.pdf`

Why this refresh made sense:
- the same dense grid structure is now anchored to a more simulation-relevant coal/ammonia flamelet comparison
- the new reference is closer to validation-style multi-panel profile work than the previous source

### `sample_0007` — two-panel validation pair
Refreshed with:
- `volume_averaged_ammonia_air_porous_media_dispersion.pdf`

Why this refresh made sense:
- the two-panel validation-pair pattern is now tied to a simulation-heavy porous-media comparison instead of an older experimental anchor
- it remains broad enough for model-vs-reference work across domains

## Current high-weight watchlist

These papers still matter, but they are better treated as watched influences than as immediate promotions:

- `1-s2.0-S1540748925001804-main.pdf` — strong counterflow dual-fuel profile paper; currently better as line-family judgment than as a direct canonical replacement
- `1-s2.0-S1540748925001762-main.pdf` — strong DNS dual-fuel swirl paper with conditional mean/std and contour structure; currently better as a composite watchlist paper than as a direct sample refresh
- `1-s2.0-S1540748924003080-main.pdf` — useful LES differential-diffusion validation source; currently sharpens judgment more than it defines a new starter

For the fuller map, see `../pdf/SIMULATION_CURATION.md`.

## What should probably stay as-is for now

- `sample_0004` still seems like a good inset-specific starter
- `sample_0006` still seems like a useful parameter-scan / branch template
- `sample_0014` still seems like a strong stacked-shared-x starter unless a clearer simulation analogue appears

## Curation attitude

When a newer simulation paper has the same structural idea as an older, less relevant paper, the newer one should usually carry more weight.
That does **not** mean replacing everything immediately.
It means:
- prefer the newer, simulation-aligned source when the structure overlaps strongly
- stop promoting new samples once the main reusable structures are already covered
- preserve the remaining value in `patterns/` and PDF curation notes rather than in more scripts

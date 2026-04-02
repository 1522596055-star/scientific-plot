# multi-panel patterns

Distilled guidance for figures with two or more coordinated subplots.

The goal of this note is to reduce noise in the busiest part of the library: not every paper with multiple panels should become a new sample, but many papers contain strong layout ideas worth preserving.
These are soft tendencies and recurring patterns, not rigid rules.

## Canonical starter templates

These are the main multi-panel starters an agent should try first.

### `sample_0014` — vertically stacked shared-x metrics
Use first when:
- two metrics share the same x-axis
- the figure should read top-to-bottom as one experimental story
- separate y-scales are needed but the panels should remain tightly linked

Why it is canonical:
- this is one of the most reusable publication layouts for applied data
- it solves the common decision of "separate panels vs overloaded twin-axis figure"

### `sample_0003` — dense small-multiple grid with simulation vs reference profiles
Use first when:
- several species, targets, or metrics need their own panel
- each panel repeats the same grammar: smooth model line + reference markers
- the figure is closer to a grid of coordinated scientific subplots than to one story split into two panels

Why it is canonical:
- it captures a true small-multiples pattern rather than a subject-specific figure
- it is the main starter for dense grid-based scientific layouts

### `sample_0007` — two-panel validation pair
Use first when:
- two quantities or conditions should be compared side by side
- each panel contains reference markers plus one modeled line
- one shared legend should explain both panels

Why it is canonical:
- it captures a very common paper pattern without requiring a larger grid
- it is broad enough for simulation-vs-reference, model-vs-benchmark, or experiment-vs-prediction pairs

## Secondary variants

### `sample_0002` — compact repeated validation panels
Useful when:
- the figure has several aligned panels but lighter density than a full 2x3 grid
- each panel repeats the same mean/rms or line/marker validation grammar
- the same repeated structure matters more than large per-panel customization

Why it is a variant:
- it is structurally close to the canonical grid family and should not become the first stop unless that compact 1x3 rhythm is specifically useful

### `sample_0010` — two-panel shared-x metric comparison with baselines
Useful when:
- the user needs two panels with different metrics over one x-axis
- baseline or reference lines matter
- the plot reads like an applied engineering comparison

Why it is a variant:
- it is close to `sample_0014`, but the emphasis is more on metric-specific line treatments than on the generic stacked-metric starter

## Good ideas worth reusing without creating new samples

### 1. Split panels by metric when y-scales tell different stories
This is often better than forcing multiple concepts into a twin-axis figure.
If two variables need different visual attention, stacked panels are usually clearer.

### 2. Keep visual grammar stable across panels
Good multi-panel figures repeat:
- the same color meaning
- the same line/marker meaning
- the same panel logic

If each panel needs a different visual language, the figure stops feeling coherent.

### 3. Share legends whenever possible
A single shared legend is usually better than repeating legends in every panel.
This reduces clutter and preserves panel area for the actual data.

### 4. Use small multiples when the reader should compare shapes, not absolute overlay density
When too many curves would overlap on one axis, separate panels often make the comparison more scientific, not less.

### 5. Keep per-panel annotation light
Panel letters, heavy notes, or large per-panel legends are often paper-specific details.
Keep only the structural ideas that help reuse.

### 6. Separate reference markers from modeled lines visually
In many good papers, markers and line styles communicate the reference/model distinction clearly.
That distinction is worth preserving even if other annotations are simplified away.

## When not to add another multi-panel sample

Do **not** add a new sample if the new figure only changes:
- panel titles
- subject matter
- legend wording
- minor axis-range differences

Prefer:
- reusing a canonical starter
- borrowing one variant detail
- recording the conceptual lesson in this note

## Fast selection guide

- two vertically stacked metrics over one x-axis → `sample_0014`
- dense grid of repeated panels with model lines and reference markers → `sample_0003`
- two-panel validation pair → `sample_0007`
- compact 1x3 repeated validation comparison → `sample_0002` only if specifically helpful
- two-panel metric comparison with baseline/reference-line flavor → `sample_0010` only if needed

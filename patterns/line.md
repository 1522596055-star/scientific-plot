# line patterns

Distilled guidance for single-panel line-oriented scientific figures.

The goal of this note is to keep the repository from accumulating too many near-duplicate line charts while preserving the good ideas found in published figures.
These are soft tendencies and recurring patterns, not rigid rules.

## Canonical starter templates

These are the main line templates an agent should try first.

### `sample_0013` — plain multi-line model / trend comparison
Use first when:
- one x-axis and one y-axis tell the whole story
- several methods, treatments, or rates should be overlaid cleanly
- the figure is about curve agreement, shift, decay, or profile shape rather than layout complexity

Why it is canonical:
- it is the cleanest baseline for ordinary multi-line scientific plots
- it now reflects simulation-heavy model-comparison usage without becoming domain-locked
- it is still the best starting point when the user only needs "a good paper-style line chart"

### `sample_0004` — line chart with inset zoom
Use first when:
- the main figure has a compressed low-magnitude or early-stage region
- the reader needs both the full trend and a local zoom
- a secondary top axis is scientifically meaningful

Why it is canonical:
- inset logic is common and worth preserving as a distinct starter
- it captures the decision to zoom, not just the mechanics of drawing curves

### `sample_0006` — parameter scan with branch structure
Use first when:
- the x-axis is a continuously scanned control variable
- branch behavior matters, especially stable vs unstable segments
- the figure is theoretical or mechanism-oriented rather than purely empirical

Why it is canonical:
- branch separation is a genuinely different pattern from ordinary overlays
- it prevents agents from forcing bifurcation-like behavior into a plain multi-line template

## Secondary variant

### `sample_0005` — dense overlay with dual encoding
Use only when:
- color should encode one variable and linestyle should encode another
- the figure genuinely needs many overlaid curves on one axis
- a second legend or split legend strategy is justified

Why it is **not** the default starter:
- it is more complex than most line figures need
- if used too often, agents will overproduce busy legends and over-encoded plots

## Good ideas worth reusing without creating new samples

### 1. Use inset only when it rescues a real scientific feature
Good papers use insets to reveal structure that would otherwise disappear.
Do **not** add an inset just because there is empty space in the figure.

### 2. Keep the canonical plain-line starter truly plain
A strong default line sample should usually keep:
- one x-axis
- one y-axis
- a compact legend
- clean differentiation by color and/or linestyle

If a figure needs extra axes, repeated panels, or branch logic, it probably belongs somewhere else.

### 3. Split visual encoding responsibilities deliberately
A useful line-plot pattern is:
- color = mechanism / chemistry / method family
- linestyle = condition / treatment / operating point

Reuse this only when both variables are central to interpretation.
If one encoding dimension is weak, simplify.

### 4. Reserve secondary top axes for physically meaningful alternate coordinates
A top axis is valuable when it represents a real alternate variable or transformed coordinate.
Do not add one as decoration.

### 5. Separate branch behavior instead of hiding it inside one style
For parameter scans, stable and unstable branches should usually look visibly different.
This is often better than pushing them into annotations or separate panels.

### 6. Prefer one clean legend over many tiny annotations
Published figures often contain heavy inline labels that are hard to reuse.
For a template library, preserve the structural idea and simplify the annotation burden.

## When to split into multi-panel instead of adding another line sample
Move toward `multi_panel` when:
- more than one response variable is important
- y-scales differ strongly
- more than 4–6 overlaid curves make the figure visually dense
- the figure contains repeated subplots with the same visual grammar

## Anti-patterns to avoid

- adding a new line sample just because the subject matter is different
- keeping many line variants whose only difference is legend wording
- turning every paper figure with an inset into a separate sample
- copying paper-specific annotation clutter into reusable templates

## Fast selection guide

- ordinary multi-line scientific trend or model comparison → `sample_0013`
- line chart plus inset / zoomed low region → `sample_0004`
- parameter scan / branch behavior → `sample_0006`
- dense dual-encoding overlay → `sample_0005` only if clearly needed

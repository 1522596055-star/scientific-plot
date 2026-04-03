# line

## Family thesis

A strong line family stays quiet.
Most reusable scientific line figures are not elaborate; they are careful.
The main decision is rarely “how many visual tricks should this plot have?”
It is usually one of these:
- should the figure remain a plain overlay?
- does it truly need an inset?
- is it really a branch / scan figure rather than an ordinary line chart?
- has it become dense enough that it should move to multi-panel instead?

## Canonical anchors

| Sample | Role | Use first when |
|---|---|---|
| `sample_0013` | canonical plain overlay | one axis is enough, several curves must be compared cleanly |
| `sample_0004` | canonical inset line | one local region matters enough to justify a zoom |
| `sample_0006` | canonical scan / branch figure | stable and unstable structure or branch separation is the story |
| `sample_0005` | variant dense overlay | color and linestyle both carry essential meaning |

## Fine points that matter

### Keep the default starter truly plain
For a canonical line starter, prefer:
- one x-axis
- one y-axis
- a compact legend
- differentiation by color and/or linestyle only

If the figure needs more than that, it may belong elsewhere.

### Use an inset only to rescue real structure
An inset is justified when a scientifically important region would otherwise disappear.
It is not a decorative way to fill white space.

### Separate branch behavior visibly
If a scan has stable and unstable regions, make that distinction structural.
Do not hide it in text.

### Encode with restraint
A useful hierarchy is:
- color for method / family
- linestyle for condition / treatment

If both encodings are not truly needed, simplify.

## When not to stay in this family

Move away from `line/` when:
- more than one response variable matters equally
- overlay density starts to make shapes unreadable
- y-scales differ so strongly that comparison becomes strained
- the figure is really a repeated validation layout rather than one overlay

## Representative paper lessons

- `ref/papers/archive/local_principal_component_transport_reacting_flow.pdf` — a simulation-oriented line starter can stay plain if nonessential secondary axes are removed
- `ref/papers/archive/premixed_flames_dominant_diffusion_source_mixture.pdf` — branch structure deserves its own visual grammar
- `ref/papers/inbox/counterflow_dual_fuel_flame_simulations_dcmc.pdf` — strong profile-comparison paper, better used as judgment support than as another immediate starter
- `ref/papers/inbox/early_stage_flame_acceleration_stratified_hydrogen_air.pdf` — some line figures are really theory-validation evolutions, not generic overlays

## Anti-patterns

- adding a new sample only because the subject changed
- promoting every paper with an inset into a separate template
- keeping several near-identical plain overlays with different legend wording
- letting paper-specific annotation clutter survive into a starter template

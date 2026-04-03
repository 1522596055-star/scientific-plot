# numerical_simulation

## Family thesis

Simulation-heavy plotting is not a separate chart family.
It is a **visual stance**.
The recurring difference is that these figures are often built to establish trust:
- prediction vs reference
- mean vs fluctuation
- field structure vs extracted cuts
- accuracy vs computational cost

That means the repository should weight simulation papers heavily, but still promote only a few clean reusable structures.

## The current simulation-facing anchors

| Sample | Why it now carries the family |
|---|---|
| `sample_0013` | the plain line starter now reflects reduced-order model comparison without losing simplicity |
| `sample_0002` | the compact repeated-panel starter now reflects conditional-profile validation in ammonia-flame LES |
| `sample_0003` | the dense grid starter now reflects flamelet-style thermo-chemical validation |
| `sample_0007` | the two-panel starter now reflects porous-media model-vs-reference validation |
| `sample_0006` | the branch / scan starter still covers theory-heavy and mechanism-heavy simulation scans well |

## The visual stance to preserve

### Prefer validation grammar over decoration
Typical simulation figures benefit from:
- compact legends
- explicit normalization
- clean model vs reference distinction
- minimal annotation clutter

### Treat mean and fluctuation as first-class when needed
If rms, spread, or conditional fluctuation is part of the scientific claim, let it appear structurally.
Do not collapse everything into one mean line by habit.

### Keep field and profile views conceptually linked
When a task sounds spatial and validation-heavy, think in terms of field + cut rather than choosing only one.

### Stop promoting once the main structures are covered
The current repository already has good anchors for the most reusable simulation-facing forms.
From here on, pattern extraction should usually outrank sample proliferation.

## Current watchlist

| Paper | Why it is still worth watching |
|---|---|
| `ref/papers/inbox/counterflow_dual_fuel_flame_simulations_dcmc.pdf` | strong line-family judgment source; not yet the cleanest direct canonical replacement |
| `ref/papers/inbox/dns_liquid_ammonia_methane_dual_fuel_swirl_combustion.pdf` | combines conditional profiles with combustion-mode contours; likely more valuable as a composite influence than as an immediate refresh |
| `ref/papers/inbox/differential_diffusion_les_turbulent_premixed_flames.pdf` | sharpens simulation-profile judgment without yet demanding its own starter |

## Decision rule

When a new simulation paper arrives, ask:
1. does it preserve an existing reusable structure already covered by `samples/`?
2. is it clearly a better anchor than the current one?
3. if not, is its real value better captured in `patterns/` or in `ref/papers/SIMULATION.md`?

The default should now be selectivity, not expansion.

## Companion document

For the fuller paper-by-paper review, read:
- `../ref/papers/SIMULATION.md`

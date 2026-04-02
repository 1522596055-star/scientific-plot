# simulation PDF curation

A full-review map of the repository's current simulation-heavy paper set.

This file exists so the repository can absorb many simulation-oriented PDFs without forcing all of them into new samples.
It is the bridge between:
- refreshed canonical samples in `samples/`
- soft pattern notes in `patterns/`
- the still-untriaged queue in `pdf/inbox/`

Use this file when the task is explicitly simulation-heavy or when deciding whether a new simulation paper should refresh an existing sample, remain a pattern note, or stay archive-only.

## Current repository stance after the full review

The repository now has enough simulation-aligned anchors in the most important reusable families.
That means the default posture should be:
- **refresh only when the structural overlap is very strong**
- **prefer pattern extraction over creating more near-duplicate samples**
- **keep the inbox as a watchlist, not a backlog of mandatory promotions**

## Simulation-aligned curated anchors already in the archive

These papers now define the simulation-facing center of gravity of the sample library.

| Curated PDF | Related sample | Why it matters |
|---|---|---|
| `four_fuel_stream_flamelet_pulverized_coal_ammonia_combustion.pdf` | `sample_0003` | Best current anchor for dense grid-based validation profiles with repeated model-vs-reference grammar. |
| `large_eddy_simulation_partially_cracked_ammonia_flames.pdf` | `sample_0002` | Strong compact 1x3 validation-panel rhythm with repeated conditional-profile logic. |
| `volume_averaged_ammonia_air_porous_media_dispersion.pdf` | `sample_0007` | Strong two-panel validation pair where each panel isolates one dominant quantity and compares model vs reference. |
| `local_principal_component_transport_reacting_flow.pdf` | `sample_0013` | Strong canonical plain multi-line anchor for simulation-oriented model comparisons that still stays visually simple. |
| `premixed_flames_dominant_diffusion_source_mixture.pdf` | `sample_0006` | Still the best branch / parameter-scan anchor for theory-heavy and mechanism-heavy simulation plots. |
| `ammonia_methanol_diesel_rcci_marine_engines.pdf` | `sample_0014` | Useful stacked-metric anchor for engineering-style simulation / experiment response comparisons over one control axis. |

## High-weight pending watchlist

These papers are still the most likely future refresh or expansion candidates.
They matter because their structure overlaps with important simulation-heavy use cases, but they do **not** yet justify another promotion.

| Inbox PDF | Current best home | Why it is still being watched |
|---|---|---|
| `1-s2.0-S1540748925001804-main.pdf` | line-family judgment note | Counterflow dual-fuel profile comparisons are scientifically strong, but the paper is not the cleanest direct replacement for the canonical plain multi-line starter. |
| `1-s2.0-S1540748925001762-main.pdf` | composite / validation watchlist | DNS of liquid ammonia/methane dual-fuel swirl combustion combines conditional mean/std profiles with heat-release contours; structurally strong, but not a clear one-to-one replacement for an existing sample. |
| `1-s2.0-S1540748924003080-main.pdf` | simulation-profile pattern note | Differential-diffusion LES adds good field-plus-profile validation ideas, but it currently sharpens judgment more than it defines a new reusable starter. |

## Pattern-only simulation contributors

These papers are important, but their main value is in shaping judgment rather than creating more sample directories.

### A. Field + profile comparison papers
These papers reinforce the idea that simulation figures are often strongest when they combine spatial structure with one or more quantitative cuts.

| Inbox PDF | Main takeaway | Best landing place |
|---|---|---|
| `1-s2.0-S1540748924000117-main.pdf` | Spray-LES paper with OH/HRR images, evaporation summaries, and field comparisons. Good reminder that field snapshots plus downstream summary profiles often communicate better than one chart alone. | `patterns/composite.md` + `patterns/numerical_simulation.md` |
| `1-s2.0-S1540748924001196-main.pdf` | DNS + flamelet modeling paper mixing field snapshots, scatter in mixture-fraction space, and profile validation. Strong evidence for field+scatter+profile composites. | `patterns/composite.md` |
| `1-s2.0-S1540748924003225-main.pdf` | Supercritical flame paper emphasizing field interpretation, regime structure, and phase-aware thermochemical maps. | `patterns/composite.md` |
| `1-s2.0-S1540748925001713-main.pdf` | PINN species-reconstruction paper reinforcing side-by-side field reconstruction with profile comparison. | `patterns/composite.md` |

### B. Workflow / surrogate / solver-comparison papers
These papers are scientifically useful, but their reusable value is mostly conceptual: how to show accuracy, cost, or model structure without turning the library into a solver-benchmark collection.

| Inbox PDF | Main takeaway | Best landing place |
|---|---|---|
| `1-s2.0-S1540748924001214-main.pdf` | ML-enhanced LES paper with scatter clouds, field views, and a-posteriori comparison. Reminds us that many solver-improvement figures are validation composites, not starter templates. | `patterns/composite.md` + `patterns/numerical_simulation.md` |
| `1-s2.0-S1540748924002487-main.pdf` | Quantum-computing reacting-flow paper emphasizing solver-accuracy and complexity comparisons. Better as workflow/performance judgment than as a plotting sample. | `patterns/composite.md` |
| `1-s2.0-S1540748924003201-main.pdf` | Simulation-tooling workflow / architecture / performance-comparison figures. Valuable conceptually, not as a direct sample. | `patterns/composite.md` |
| `1-s2.0-S1540748924003596-main.pdf` | Uncertainty-propagation paper with parity plots, uncertainty bands, and Sobol-style importance summaries. Useful as a future uncertainty-pattern source, not a current sample. | `patterns/composite.md` |
| `1-s2.0-S1540748925000100-main.pdf` | Review-style scientific-machine-learning figures for combustion. Valuable for synthesis and framing, not for a new plotting template. | `patterns/composite.md` |

### C. Transient / instability / event-sequence papers
These papers matter mainly because they show how simulation outputs pair with cycle timing, snapshots, or evolving structures.

| Inbox PDF | Main takeaway | Best landing place |
|---|---|---|
| `1-s2.0-S1540748924000877-main.pdf` | Plasma + thermoacoustics paper combining pressure traces, HRR, chemiluminescence, PLIF, and LES snapshots. Excellent composite guidance. | `patterns/composite.md` |
| `1-s2.0-S1540748924001962-main.pdf` | Field snapshots + probability distributions + inset-rich transient analysis. | `patterns/composite.md` |
| `1-s2.0-S1540748924004401-main.pdf` | Transient event sequence with diagnostics and regime evolution. | `patterns/composite.md` |
| `1-s2.0-S1540748924005765-main.pdf` | Field snapshots + temporal spectra + averaged fields. | `patterns/composite.md` |
| `1-s2.0-S1540748925000410-main.pdf` | Transient leading-edge evolution with phase segmentation and contour snapshots. | `patterns/composite.md` |

### D. Narrow but still useful simulation line / profile papers
These are worth remembering, but they are too specialized to become default starters right now.

| Inbox PDF | Main takeaway | Best landing place |
|---|---|---|
| `1-s2.0-S1540748924000890-main.pdf` | Theory + simulation flame-acceleration curves are a reminder that some simulation line figures are really parameter-evolution or theory-validation charts. | `patterns/line.md` + `patterns/numerical_simulation.md` |
| `1-s2.0-S1540748924004073-main.pdf` | Centerline profiles and parametric sensitivity in TiO2 flame synthesis. Useful scientifically, but existing line families already cover the reusable structure. | line-family judgment note |
| `1-s2.0-S154074892400525X-main.pdf` | Radial droplet profiles and parametric sweeps for aluminum combustion. Interesting, but too narrow to promote now. | line-family judgment note |
| `1-s2.0-S1540748925001117-main.pdf` | Phase-change / droplet-evolution line figures with component histories and lifetime summaries. Good narrow line inspiration. | line-family judgment note |

## Simulation papers that currently stay outside the main watchlist

These are still useful, but they are not where the repository should spend the next sample-promotion effort.

- `1-s2.0-S1540748925000495-main.pdf` — strongest value remains line/scatter judgment for ignition-delay-like comparisons
- `1-s2.0-S1540748924004462-main.pdf` — stronger as conceptual comparison / review guidance than as a direct simulation template
- `1-s2.0-S1540748918306345-main.pdf` — broad ammonia-combustion review, helpful for judgment but not for one plotting structure

## Practical curation rule after this review

When a new simulation paper arrives, ask these questions in order:
1. does it preserve an existing reusable structure already present in `samples/`?
2. if yes, is it clearly more aligned with the group's real workflow than the current anchor?
3. if not, does it still teach a recurring visual idea worth distilling into `patterns/`?
4. if not, keep it in `pdf/inbox/` as retained evidence rather than promoting it automatically

## Recommended reading order for future simulation-heavy curation

1. `../patterns/numerical_simulation.md`
2. `../patterns/composite.md` if field maps, snapshots, or workflow figures are involved
3. `../samples/REFRESH_CANDIDATES.md`
4. this file
5. only then browse raw PDFs in `pdf/` or `pdf/inbox/`

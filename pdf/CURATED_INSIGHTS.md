# curated PDF insights

Soft takeaways distilled from the already curated PDF archive.

This file is not meant to impose rigid rules.
Its purpose is to preserve the kinds of visual judgment that repeatedly appear in published figures, while still leaving room for case-by-case interpretation.

## How to read this file

For each archived paper below, the useful output is not just the selected sample.
It is also the broader idea the paper reinforces:
- what kind of figure structure tends to work well
- what should stay as a canonical starter
- what should remain a narrower variant
- what is worth remembering even when the exact figure is not reused

## Archived papers and their reusable takeaways

| PDF | Related sample(s) | Soft takeaway |
|---|---|---|
| `premixed_flames_dominant_diffusion_source_mixture.pdf` | `sample_0006` | A parameter scan can be clearer than a plain multi-line overlay when branch behavior matters. Stable and unstable segments often deserve visibly different treatments. |
| `soot_precursors_pmlf_pentamethyl_heptane.pdf` | former `sample_0007` anchor | A two-panel measured-vs-modeled comparison works well when each panel tells the same kind of story under a different condition. Shared legend logic often keeps the figure cleaner. |
| `nh_no_plif_plasma_assisted_nh3_h2_flames.pdf` | `sample_0008` | Signed horizontal bars can be a better summary than many small line plots when the real message is ranked effect size or sensitivity direction. |
| `ir_hychem_infrared_aviation_fuels.pdf` | `sample_0009` | Sensitivity and parameter-importance plots often read best as compact bar summaries, especially when the ranking matters more than a continuous trend. |
| `equivalence_ratio_dual_fuel_ammonia_diesel_engine.pdf` | `sample_0010` | Two vertically linked panels can be more readable than a single overloaded plot when different response variables share the same control axis but need different y-scales. |
| `extinction_limits_hydrocarbon_ammonia_diffusion_flames.pdf` | `sample_0011` | Sparse scientific comparisons are often better left as point plots. A line would imply continuity that the underlying measurements may not really support. |
| `cycloalkane_additives_hefa_pyrolysis_ignition.pdf` | `sample_0012` | When ignition-delay-like quantities span decades, log-scale point plots can feel much more natural than linear-scale curves. The important idea is often cross-series separation, not line smoothness. |
| `polymer_pyrolysis_lumped_models_pmma_pom.pdf` | former `sample_0013` anchor | A plain multi-line chart remains a strong default when the figure is really about smooth shift between curves rather than extra layout complexity. |
| `four_fuel_stream_flamelet_pulverized_coal_ammonia_combustion.pdf` | `sample_0003` | Dense multi-panel validation grids become more reusable when each panel preserves the same model-versus-reference grammar and avoids excessive per-panel customization. |
| `local_principal_component_transport_reacting_flow.pdf` | `sample_0013` | A canonical single-axis line starter can still be simulation-relevant if it stays visually plain and drops paper-specific secondary axes that are not essential for reuse. |
| `large_eddy_simulation_partially_cracked_ammonia_flames.pdf` | `sample_0002` | A compact repeated-panel layout is valuable when several axial locations or conditions repeat the same validation grammar but do not justify a full dense grid. |
| `volume_averaged_ammonia_air_porous_media_dispersion.pdf` | `sample_0007` | Two-panel validation pairs remain highly reusable when each panel isolates one dominant quantity and preserves a simple reference-versus-model distinction. |
| `ammonia_methanol_diesel_rcci_marine_engines.pdf` | `sample_0014` | Stacked shared-x panels are especially effective when one operating variable governs multiple linked responses. This is often more publication-like than twin axes. |

## Pattern-level themes reinforced by the curated archive

### Line family
The curated archive reinforces that most reusable single-panel line figures fall into a small number of structures:
- plain multi-line trend or model comparison
- inset-driven line view
- parameter scan with branch behavior
- denser dual-encoding overlay only when necessary

### Multi-panel family
The curated archive reinforces that most reusable multi-panel figures can be organized around a few stable layouts:
- vertically stacked shared-x metrics
- two-panel validation pairs
- compact repeated validation panels
- denser small-multiple grids only when the number of targets truly requires them

### Scatter family
The curated archive reinforces that sparse scientific measurements should not automatically be turned into lines.
Sometimes the strongest choice is simply a well-organized point comparison.

### Bar family
The curated archive reinforces that bar charts remain useful when the scientific question is really about ranking, signed direction, or category-level comparison rather than continuous dynamics.

## What this file is not

This file is not a promotion mechanism.
If a future task suggests a different chart is better, that is still allowed.
These notes are meant to sharpen judgment, not replace it.

For the fuller simulation-heavy review across both the archive and the inbox, see `SIMULATION_CURATION.md`.

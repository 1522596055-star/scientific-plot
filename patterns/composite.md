# composite

## Family thesis

Composite figures are justified when one chart cannot carry the scientific story by itself.
They should be used with discipline.
The right question is not “can this paper figure be copied?”
It is “what combination of views is actually necessary here?”

## Recurrent composite modes

### 1. Field + profile
Use when a spatial or image-like result needs a quantitative cut beside it.
This is one of the most valuable composite patterns for simulation-heavy work.

### 2. Time series + event imagery
Use when the timing of visible physical changes matters.
Typical structure: a strip of key frames above aligned traces.

### 3. Schematic + one main plot
Use when geometry, diagnostic placement, or apparatus layout is essential to interpretation.
The schematic should support the data, not overpower it.

### 4. Accuracy + cost / complexity
Use when the real message is a tradeoff between predictive quality and computational burden.
This belongs more often in a note than in a reusable starter.

### 5. Regime map / response surface
Use when two control variables define the story more naturally than a family of many line plots.

## Fine points that matter

### Keep the chart burden clear
If the composite includes a schematic, field view, or image strip, the quantitative chart still needs to remain readable on its own.

### Match sampling logic across panels
For field + profile composites, the relationship between the field view and the extracted cut should be explicit.

### Do not promote heterogeneity into a starter too quickly
Many excellent composite figures are too paper-specific to become templates.
Often the better result is a sharper note, not another sample directory.

## Current strong references

- `ref/papers/inbox/les_n_heptane_n_dodecane_binary_blend_spray_flames.pdf` — field views paired with downstream evaporation summaries
- `ref/papers/inbox/dns_flamelet_alkali_metal_emissions_pulverized_biomass.pdf` — field + scatter + profile mixture
- `ref/papers/inbox/plasma_stabilization_sequential_combustor_les_experiments.pdf` — time traces, imaging, and LES snapshots in one scientific narrative
- `ref/papers/inbox/les_battery_vent_gas_flame_ignition_anchoring.pdf` — transient ignition and anchoring with image-like context
- `ref/papers/inbox/pinn_reacting_flows_species_reconstruction_sparse_velocity.pdf` — field reconstruction beside profile comparison
- `ref/papers/inbox/uncertainty_hydrogen_flameless_combustion_furnace_surrogate_simulation.pdf` — uncertainty and sensitivity composites

## Promotion rule

A composite should remain in `patterns/` unless the same structural combination appears repeatedly enough to justify a dedicated template.
The default answer should be patience.

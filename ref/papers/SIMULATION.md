# simulation paper curation

A paper-by-paper map of the repository’s simulation-heavy reference set.

This note exists to prevent two opposite mistakes:
- promoting every simulation paper into a sample
- forgetting what the non-promoted papers still taught us

## Curation stance

The repository already has strong simulation-facing anchors for its main reusable structures.
That means the default stance should now be:
- promote rarely
- refine patterns carefully
- keep the inbox as a watchlist, not a backlog

## Current archive anchors

| Archived paper | Current role |
|---|---|
| `four_fuel_stream_flamelet_pulverized_coal_ammonia_combustion.pdf` | dense-grid validation anchor (`sample_0003`) |
| `large_eddy_simulation_partially_cracked_ammonia_flames.pdf` | compact repeated-panel anchor (`sample_0002`) |
| `volume_averaged_ammonia_air_porous_media_dispersion.pdf` | two-panel validation-pair anchor (`sample_0007`) |
| `local_principal_component_transport_reacting_flow.pdf` | plain simulation-oriented line anchor (`sample_0013`) |
| `premixed_flames_dominant_diffusion_source_mixture.pdf` | branch / scan anchor (`sample_0006`) |
| `ammonia_methanol_diesel_rcci_marine_engines.pdf` | stacked-metric engineering anchor (`sample_0014`) |

## Watchlist papers

These still deserve attention, but not immediate promotion.

| Inbox paper | Why it remains on watch |
|---|---|
| `counterflow_dual_fuel_flame_simulations_dcmc.pdf` | strong line-family judgment source, especially for profile comparisons |
| `dns_liquid_ammonia_methane_dual_fuel_swirl_combustion.pdf` | strong field + conditional-profile paper, likely more useful as a composite influence than as a direct sample refresh |
| `differential_diffusion_les_turbulent_premixed_flames.pdf` | strong LES validation paper that sharpens profile judgment |

## Pattern-level contributors

### Field + profile contributors
- `les_n_heptane_n_dodecane_binary_blend_spray_flames.pdf`
- `dns_flamelet_alkali_metal_emissions_pulverized_biomass.pdf`
- `supercritical_ch4_o2_flame_structure_simulation.pdf`
- `pinn_reacting_flows_species_reconstruction_sparse_velocity.pdf`

These reinforce the idea that many simulation figures work best when spatial structure and quantitative cuts appear together.

### Workflow / accuracy / complexity contributors
- `machine_learning_filtered_flame_front_displacement_les.pdf`
- `quantum_computing_reacting_flows_hamiltonian_simulation.pdf`
- `gpu_machine_learning_reactive_flow_acceleration_framework.pdf`
- `uncertainty_hydrogen_flameless_combustion_furnace_surrogate_simulation.pdf`
- `scientific_machine_learning_combustion_discovery_simulation_control.pdf`

These are valuable, but usually as judgment about composite structure rather than as starters.

### Transient / instability contributors
- `plasma_stabilization_sequential_combustor_les_experiments.pdf`
- `detonation_confinement_statistics_hydrogen_oxygen.pdf`
- `les_battery_vent_gas_flame_ignition_anchoring.pdf`
- `adaptive_mesh_refinement_methane_pool_fires.pdf`
- `les_transient_leading_edge_lifted_hydrogen_jet_flame.pdf`

These reinforce timing, event-sequence, and field-evolution composite ideas.

### Narrow line / profile contributors
- `early_stage_flame_acceleration_stratified_hydrogen_air.pdf`
- `tio2_production_laminar_coflow_diffusion_flame_simulation.pdf`
- `aluminum_droplet_combustion_hot_steam_simulation_experiments.pdf`
- `ammonia_droplet_phase_change_water_vapor_molecular_dynamics.pdf`

These matter scientifically, but not enough to become default starters right now.

## Decision rule

When a new simulation paper arrives, ask:
1. does it preserve a reusable structure already represented in `samples/`?
2. is it clearly a better anchor than the current one?
3. if not, is its main value better captured in `patterns/`?

If the answer to the first two questions is not clearly yes, do not promote it just because it is simulation-heavy.

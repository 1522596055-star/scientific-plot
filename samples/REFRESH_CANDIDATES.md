# sample refresh candidates

This file tracks where simulation-weighted refresh work currently stands.

The main goal of the recent refresh wave was to replace older anchors when a newer paper preserved the same reusable structure while matching the group's research context better.
These are soft notes, not irreversible rules.

## Recently refreshed samples

### `samples/line/sample_0013/`
Status:
- refreshed using `pdf/local_principal_component_transport_reacting_flow.pdf`

Why this refresh was chosen:
- the new paper preserved the clean single-axis multi-line pattern
- it provided a stronger simulation-oriented anchor than the former polymer-decomposition reference

### `samples/multi_panel/sample_0002/`
Status:
- refreshed using `pdf/large_eddy_simulation_partially_cracked_ammonia_flames.pdf`

Why this refresh was chosen:
- the new paper supplied a compact repeated validation-panel rhythm
- it stayed structurally distinct from the denser canonical grid in `sample_0003`

### `samples/multi_panel/sample_0003/`
Status:
- refreshed using `pdf/four_fuel_stream_flamelet_pulverized_coal_ammonia_combustion.pdf`

Why this refresh was chosen:
- the new source preserved the same reusable dense-grid structure
- it is closer to the group's simulation-heavy coal/ammonia workflow than the previous reference

### `samples/multi_panel/sample_0007/`
Status:
- refreshed using `pdf/volume_averaged_ammonia_air_porous_media_dispersion.pdf`

Why this refresh was chosen:
- the two-panel validation-pair structure now has a more simulation-relevant anchor
- it remains reusable across model-vs-reference tasks, not just one subject domain

## No immediate first-tier refreshes remain

After the current review, the main reusable simulation-facing structures already have stronger anchors.
That means the repository should now be more selective.

## Watched papers that could matter later

### `pdf/inbox/1-s2.0-S1540748925001804-main.pdf`
Current best home:
- line-family judgment note for now

Why it is still worth watching:
- it contains strong counterflow dual-fuel profile comparisons
- it may justify a future narrow line/profile variant if that structure keeps recurring
- it was not the cleanest direct replacement for the canonical plain multi-line starter

### `pdf/inbox/1-s2.0-S1540748925001762-main.pdf`
Current best home:
- composite / validation watchlist

Why it is still worth watching:
- it combines conditional mean/std profiles with contour-based combustion-mode views
- it is highly relevant scientifically, but its strongest value may be as a field+profile composite influence rather than a direct sample refresh

### `pdf/inbox/1-s2.0-S1540748924003080-main.pdf`
Current best home:
- simulation-profile judgment note

Why it is still worth watching:
- it offers strong LES differential-diffusion profile comparisons
- it may sharpen a future simulation-profile variant if repeated tasks demand it

## What probably should not be touched next without a stronger reason

- `sample_0004` — still useful as the dedicated inset starter
- `sample_0006` — still useful as the parameter-scan / branch starter
- `sample_0014` — still useful as the stacked-shared-x metrics starter

## Working principle

When refreshing a sample:
1. replace the old reference only if the new paper preserves the same reusable structure
2. update the README and `meta.json` to explain why the new source is now the better anchor
3. avoid creating duplicate near-equivalent samples when a refresh is enough
4. once the main structures are well covered, prefer pattern extraction over more refreshes

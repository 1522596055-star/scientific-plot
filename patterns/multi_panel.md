# multi_panel

## Family thesis

Multi-panel figures should earn their complexity.
The useful split is not “one panel vs many panels.”
It is usually one of these:
- one experimental story told through stacked metrics
- one quantity repeated across several locations or conditions
- one dense validation grid with shared grammar
- one paired comparison where two panels are enough

## Canonical anchors

| Sample | Role | Use first when |
|---|---|---|
| `sample_0014` | canonical stacked metrics | two linked responses share one x-axis |
| `sample_0003` | canonical dense grid | many quantities need coordinated panels with the same validation grammar |
| `sample_0007` | canonical validation pair | two panels are enough and each compares one model line against one reference set |
| `sample_0002` | variant compact repeat | a light 1x3 repeated validation rhythm is the real structural idea |
| `sample_0010` | variant shared-x engineering comparison | baseline/reference-line treatments matter more than the generic stacked layout |

## Fine points that matter

### Keep panel grammar stable
A good multi-panel figure repeats meaning cleanly:
- color meaning
- marker meaning
- panel logic
- legend logic

If each panel behaves differently, the figure stops feeling reusable.

### Share legends whenever possible
A single shared legend is usually cleaner than repeated legends in every panel.
Panel area is expensive.

### Use grids only when the number of quantities justifies them
Dense grids are powerful, but only when several coordinated views are truly needed.
Do not upgrade a compact figure into a grid just because the paper did.

### Treat validation pairs as their own pattern
Two-panel model-vs-reference figures are common enough to deserve a dedicated anchor.
They are not simply “small grids.”

## When not to add another multi-panel sample

Do not promote a new sample if the new figure changes only:
- panel titles
- domain topic
- legend wording
- minor axis ranges

Usually the right move is to:
- reuse a canonical starter
- borrow one detail from a variant
- record the lesson in this note

## Representative paper lessons

- `ref/papers/archive/four_fuel_stream_flamelet_pulverized_coal_ammonia_combustion.pdf` — dense grids stay reusable when each panel preserves the same model-vs-reference grammar
- `ref/papers/archive/large_eddy_simulation_partially_cracked_ammonia_flames.pdf` — compact repeated validation panels can be valuable without becoming a full grid
- `ref/papers/archive/volume_averaged_ammonia_air_porous_media_dispersion.pdf` — a two-panel validation pair is often enough when each panel isolates one dominant quantity
- `ref/papers/archive/ammonia_methanol_diesel_rcci_marine_engines.pdf` — stacked shared-x metrics are often cleaner than a crowded twin-axis plot

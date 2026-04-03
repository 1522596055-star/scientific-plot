# patterns

Pattern notes sit between the sample library and the raw reference archive.

They exist for one reason:
**many good paper figures teach useful judgment without deserving another template directory.**

## What belongs here

A pattern note should capture:
- a recurring structural decision
- a small set of reliable starter samples
- the fine points that make the family work
- the boundary between “worth templating” and “worth only remembering”

A pattern note should **not** become a loose essay or a paper dump.
Its job is to make retrieval quieter and cleaner.

## Current notes

| Note | Use it for |
|---|---|
| `line.md` | single-panel scientific line figures, including inset and branch decisions |
| `multi_panel.md` | stacked layouts, validation pairs, compact repeats, and dense grids |
| `composite.md` | chart + field, chart + schematic, chart + image, and mixed scientific figures |
| `numerical_simulation.md` | simulation-heavy plotting judgment, especially validation-oriented work |

## Working order for agents

1. read the family note first
2. choose a canonical starter in `samples/`
3. open executable variants only when their narrower structure is clearly useful
4. consult `reference-samples/` if a non-reproducible paper figure would still sharpen the result
5. read raw references only if the pattern note, templates, and reference-only samples still leave a real gap

## Where the references now live

The raw paper layer is under:
- `../ref/papers/archive/`
- `../ref/papers/inbox/`

The most useful curation companions are:
- `../reference-samples/README.md`
- `../ref/papers/INSIGHTS.md`
- `../ref/papers/SIMULATION.md`
- `../samples/REFRESH_CANDIDATES.md`

## Promotion discipline

When a new paper arrives, ask:
1. does it add a genuinely new reusable structure?
2. if not, does it sharpen an existing family note?
3. if not, should it simply remain in the reference archive?

The default should be restraint.

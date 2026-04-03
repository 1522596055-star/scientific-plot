# reference-samples

Curated paper figures that are worth keeping **even when they cannot be turned into a clean executable template**.

This layer exists for figures that are:
- structurally valuable
- visually instructive
- still useful in real work
- but not honestly reproducible from the material available in the repository

## What belongs here

A reference-only sample should be kept only when all of these are true:
1. the figure teaches a real layout, comparison, or annotation decision
2. the repository does not have enough source data to rebuild it well
3. reducing it to one sentence in `patterns/` would throw away too much value

## Contract

Each reference-only sample contains:
- `reference.png` — the selected image or curated crop / montage
- `meta.json` — machine-readable guidance
- `README.md` — what to borrow and what not to copy

It does **not** contain:
- `plot.py`
- `output.png`

## How to use this layer

Agents and humans should usually work in this order:
1. read `patterns/`
2. start from an executable template in `samples/`
3. consult `reference-samples/` only when a non-reproducible paper figure still offers valuable visual guidance
4. fall back to the broader `ref/` archive only if necessary

## Families

- `line/` — non-reproducible but valuable line-oriented figures
- `multi_panel/` — non-reproducible panel layouts worth keeping as visual references
- `composite/` — mixed figures combining fields, profiles, diagnostics, or image-like panels

## Path pattern

```text
reference-samples/<family>/<reference_id>/
```

Example:

```text
reference-samples/composite/reference_0003/
```

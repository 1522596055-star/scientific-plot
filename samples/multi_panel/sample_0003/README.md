# sample_0003

## Reuse this sample when
- when you need a dense grid of simulation-versus-reference profile comparisons
- when each panel shows one quantity over the same spatial coordinate
- when the same line-plus-marker grammar repeats across all panels

## What pattern this script implements
This sample is a reusable template for a **2x3 multi-panel validation grid with model lines and reference markers**.

## Data shape expected by this script
- one `line` series and one `point` series per panel
- shared x-axis meaning across all panels
- panel-specific y-ranges for each thermo-chemical quantity

## How to adapt it
- replace the panel titles, labels, and limits in `plot.py`
- reuse `profile_series_v1.csv` with panel-specific `line` and `point` rows
- keep the repeated visual grammar stable across panels
- use background zone shading only when it carries real physical meaning

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/profile_series_v1.csv`

## Figure group used here
- `flamelet_validation_profiles`

## Run this sample
From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 samples/multi_panel/sample_0003/plot.py
```

## Output path
```text
samples/multi_panel/sample_0003/output.png
```

## Do not use this sample when
- when no repeated panel structure is needed
- when one single quantity on one axis is enough
- when uncertainty bars are the central visual feature and should dominate the comparison

## Closest sibling samples
- `sample_0002`
- `sample_0007`
- `sample_0010`
- `sample_0014`

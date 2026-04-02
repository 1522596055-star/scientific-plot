# sample_0009

## Reuse this sample when
- when two temperatures, regimes, or operating points should be compared
- when the figure is primarily about ranking positive vs negative effects
- when a compact publication-style sensitivity plot is needed

## What pattern this script implements
This sample is a reusable template for a **two-panel horizontal sensitivity chart for parameter importance**.

## Data shape expected by this script
- panel-specific category/value rows
- zero-centered signed values
- optional ordering already decided before plotting

## How to adapt it
- reuse the same horizontal-bar logic with a different `figure_group`
- replace variable names and values in `categorical_measurements_v1.csv`
- tune the color convention if positive/negative meaning changes

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/categorical_measurements_v1.csv`

## Figure group used here
- `idt_sensitivity`

## Run this sample
From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 samples/bar/sample_0009/plot.py
```

## Output path
```text
samples/bar/sample_0009/output.png
```

## Do not use this sample when
- when your chart is not signed around zero
- when a line-based sensitivity plot would communicate trends better

## Closest sibling samples
- `sample_0001`
- `sample_0008`

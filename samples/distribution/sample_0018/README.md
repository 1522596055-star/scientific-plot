# sample_0018

## Reuse this sample when
- when you need a univariate distribution view
- when only one continuous measurement is being summarized
- when bin counts are more useful than smoothed density

## What pattern this script implements
This sample is a reusable template for a **histogram for one-dimensional measurements**.

## Data shape expected by this script
- one raw numeric value per row
- a single measurement variable
- enough samples for a stable histogram shape

## How to adapt it
- replace the raw values in `distribution_measurements_v1.csv`
- change bin count and axis labels in `plot.py`
- optionally normalize the histogram if the target figure uses density instead of count

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/distribution_measurements_v1.csv`

## Figure group used here
- `particle_size_histogram`

## Run this sample
From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 samples/distribution/sample_0018/plot.py
```

## Output path
```text
samples/distribution/sample_0018/output.png
```

## Do not use this sample when
- when you need per-group comparison across many categories
- when density estimation or quartiles matter more than bin counts

## Closest sibling samples
- `sample_0016`
- `sample_0017`

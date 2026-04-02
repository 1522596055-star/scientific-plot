# sample_0019

## Reuse this sample when
- when both position and point size carry information
- when clusters or groups should be visually separated in 2D
- when embedding-style plots or bubble charts are needed

## What pattern this script implements
This sample is a reusable template for a **clustered bubble scatter plot**.

## Data shape expected by this script
- point rows with x, y, and size
- a group or cluster ID per point
- enough separation between groups to justify a legend

## How to adapt it
- replace x, y, and size values in `scatter_points_v1.csv`
- change group colors and legend names in `plot.py`
- scale marker sizes if the target publication uses a different visual range

## Files
- `plot.py` — the plotting template to copy or adapt
- `output.png` — an example rendering
- `meta.json` — machine-readable description of this sample
- `README.md` — guidance on when and how to reuse this sample

## Shared data used here
- `data/shared/scatter_points_v1.csv`

## Figure group used here
- `cluster_embedding`

## Run this sample
From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 samples/scatter/sample_0019/plot.py
```

## Output path
```text
samples/scatter/sample_0019/output.png
```

## Do not use this sample when
- when marker size carries no meaning and plain scatter is enough
- when the points should be connected into trajectories or time series

## Closest sibling samples
- `sample_0011`
- `sample_0012`

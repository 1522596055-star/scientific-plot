---
name: scientific-plotter
description: Turn raw scientific data or vague plotting requests into publication-style figures by profiling the data, choosing an appropriate chart family, mining the bundled template library in this repository for structural inspiration, and producing both a rendered image and the Python script. Use this whenever the user wants a research plot, journal-style visualization, paper-like figure, or asks what chart would best show their data—even if they only provide raw CSV/TSV/XLSX data and do not know how it should be visualized.
compatibility: Requires this repository layout plus Python with matplotlib. CSV/TSV works out of the box; Excel profiling works when pandas/openpyxl are available.
---

# Scientific Plotter

Use this skill when the user wants a scientific figure that should feel **natural, clear, and publication-minded**.

This skill is not only for cases where the user already knows the chart type.
It is especially useful when the user says things like:
- “here is my raw data, what is the best way to plot it?”
- “make this look like a paper figure”
- “I don’t know whether this should be a line chart or something else”
- “please turn this dataset into a scientific-looking figure”

## Core idea

Treat the task as two stages:
1. **decide what should be plotted**
2. **use the local template library to make it look scientifically strong**

Do not force the user to pick a chart family if the data already suggests one.
Choose a strong default, then execute.

## Final output contract

Unless the user asked for a different destination, create a small output folder in the current working directory and save:
- `plot.py`
- `output.png`

The final response should include:
- the chosen chart family
- why that chart type was selected
- the template sample(s) used for inspiration
- the output script path
- the output image path
- whether the data is real or synthetic

## Important boundaries

- **Do not modify** the repository root (`../../`) unless the user explicitly asks to expand the template library itself.
- Treat this repository as a reference library, not as a runtime dependency for the user’s final deliverable.
- The generated `plot.py` should be self-contained whenever possible.
- Keep figures scientifically styled but not cluttered: restrained colors, readable labels, consistent spacing, minimal annotation overload.

## Request modes

### Mode A: explicit chart request
The user already knows the chart family or structure.

Examples:
- grouped bar chart
- two-panel line figure
- log-scale scatter plot
- heatmap with annotations

In this mode:
- honor the requested chart family unless it would be clearly misleading
- still use the template library for structural inspiration

### Mode B: exploratory chart selection
The user provides raw data, a table, or a vague goal and does **not** know what chart to use.

Examples:
- “plot this csv scientifically”
- “make a nice paper figure from this dataset”
- “help me visualize these experimental results”

In this mode:
- profile the data first
- infer the likely analytical goal
- choose one best chart family
- proceed without asking the user to make low-level plotting decisions unless the data is genuinely ambiguous

## Workflow

### 1) Normalize the request

Extract whatever is already known:
- user goal: comparison, trend, relationship, distribution, matrix, sensitivity, etc.
- chart family if explicitly requested
- likely layout: single panel, 1x2, 2x3, inset, log axis, horizontal bars, bubble scatter
- data source: local file, attached table, or no data yet
- output expectation: publication-style, scientific, journal-like, minimal, presentation-ready

If something essential is missing, ask **one concise clarifying question**.
Do not over-interview.

### 2) If the user provided tabular data and the chart is unclear, profile the data

Run:

```bash
python3 scripts/profile_tabular_data.py <data-file>
```

If useful, save the profile:

```bash
python3 scripts/profile_tabular_data.py <data-file> --output <workdir>/data_profile.json
```

Use the result to identify:
- likely x/progression columns
- numeric measure columns
- grouping/category columns
- whether observations are aggregated or repeated
- whether the data is matrix-like
- whether log scale is a good candidate

If the choice still feels ambiguous, read `references/data-to-chart-guide.md`.

### 3) Choose the chart family

In exploratory mode, prefer one strong default instead of asking the user to choose.

Good defaults:
- **bar** for aggregated category comparisons
- **boxplot** for repeated measurements within categories
- **line** for ordered or continuous progression over x
- **multi-panel line** for multiple response variables over the same x-axis
- **scatter** for relationships between numeric variables or sparse point comparisons
- **heatmap** for labeled matrices or pairwise similarity/correlation tables

Ask a clarifying question only if the wrong chart choice would materially change the meaning of the figure.

### 4) Read distilled family guidance before opening many samples

Start with:
- `../../patterns/README.md`

If the likely family is one of the crowded ones, also read:
- `../../patterns/line.md`
- `../../patterns/multi_panel.md`
- `../../patterns/composite.md` when the target mixes charts with images, schematics, or field maps
- `../../patterns/numerical_simulation.md` when the task sounds like LES/DNS/flamelet/reduced-order or simulation-vs-reference plotting
- `../../ref/papers/SIMULATION.md` when simulation-heavy reference judgment may influence template choice

Use these notes to avoid opening too many near-duplicate samples.
Prefer a **canonical starter** before browsing narrower variants.

### 5) Convert the chart plan into a structural search query

Write a short English summary that describes the **structure**, not the domain.

Examples:
- `grouped bar chart comparing two conditions across categories`
- `two-panel figure with shared x-axis and multiple line series`
- `annotated heatmap showing matrix values with row and column labels`
- `log-scale scatter plot comparing several groups`
- `boxplot comparing raw-value distributions across categories`

### 6) Search the template library

Run:

```bash
python3 scripts/find_samples.py --query "<english structural summary>" --top 5
```

Then read the best candidates:
- sample `README.md`
- sample `meta.json`
- sample `plot.py`

If category-level orientation is needed, also read:
- `../../README.md`
- `../../samples/README.md`
- the relevant category README under `../../samples/<category>/README.md`

If several samples look plausible, read:
- `references/selection-rubric.md`
- `references/data-to-chart-guide.md`

For line and multi-panel families, prefer the candidate whose `meta.json` marks it as a **canonical** starter unless the user clearly needs a variant-specific feature.
If the task is clearly simulation-oriented, give extra attention to the guidance in `../../patterns/numerical_simulation.md` and to any repository notes that identify refresh candidates from newer simulation papers.

### 7) Choose inspiration templates

Choose by **structure first**, not by subject matter.

Prefer this order:
1. chart family and layout
2. visual encoding pattern
3. axis behavior such as log scale or inset
4. figure density / complexity
5. domain similarity only as a tiebreaker

Usually use:
- one **primary template** for the overall figure structure
- at most one **secondary template** for a single isolated detail such as inset handling, error bars, log scaling, or legend treatment

Do not collage many templates together.

### 8) Build the final standalone script

The generated `plot.py` should:
- run without depending on this repository at runtime
- keep configuration near the top
- clearly declare input paths when real data is used
- use `matplotlib.use("Agg")` when headless rendering is appropriate
- save `output.png` in the same directory unless the user asked otherwise

Prefer real data when available.

If the user provided CSV/TSV/XLSX data:
- build around that file path
- perform minimal reshaping in the script if needed
- keep the reshaping readable

If the user did **not** provide data:
- use compact synthetic data only when the request is exploratory or clearly asks for a mockup/template
- clearly mark synthetic data in comments and in the final response

### 9) Render and fix

Run the generated script.

If it fails:
- fix the script
- rerun until the image is successfully produced

Before finishing, verify that both `plot.py` and `output.png` exist.

### 10) Return a concise build summary

Report:
- why this chart family was selected
- which template sample(s) were used and why
- what was changed from the template
- where `plot.py` was saved
- where `output.png` was saved
- whether the data was real or synthetic

## Styling heuristics

Aim for figures that feel like a paper figure:
- restrained palette
- readable axis labels
- consistent line widths and marker sizes
- sensible whitespace
- no gratuitous effects
- legends only when they add meaning

## Quick interpretation hints

- If the user says **compare treatments / categories**, lean toward `bar` or `distribution`
- If the user says **trend / profile / scan / versus temperature / versus time**, lean toward `line`
- If the user has **two metrics over the same x-axis**, lean toward `multi_panel`
- If the user has **sparse measured points or numeric-vs-numeric relationships**, lean toward `scatter`
- If the data is a **matrix**, lean toward `heatmap`
- If values span orders of magnitude and stay positive, consider a **log axis**

## Fail-safe behavior

If no sample is an exact match:
- choose the closest structural pattern
- say explicitly what was borrowed
- keep the output self-contained and coherent

## References

Use these when needed:
- `references/data-to-chart-guide.md`
- `references/selection-rubric.md`
- `../../patterns/README.md`
- `../../patterns/line.md`
- `../../patterns/multi_panel.md`
- `../../patterns/composite.md`
- `../../patterns/numerical_simulation.md`
- `../../ref/papers/SIMULATION.md`
- `../../README.md`
- `../../samples/README.md`
- `../../samples/REFRESH_CANDIDATES.md`

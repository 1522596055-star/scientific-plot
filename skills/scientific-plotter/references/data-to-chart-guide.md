# Data-to-chart guide

Use this guide when the user gives raw data or a vague request like "make this look scientific" and does not know what chart to use.

## Principle

Do not ask the user to choose a chart type unless the wrong choice would materially change the scientific claim.

Instead:
1. infer the data roles
2. infer the likely analytical goal
3. choose one strong default chart
4. mention the rationale briefly in the final response

## Step 1: Infer column roles

Look for:
- **x/progression columns**: time, temperature, equivalence ratio, position, concentration, index, cycle, wavelength
- **measure columns**: numeric responses such as efficiency, yield, delay, signal, intensity, conversion
- **group columns**: fuel, catalyst, method, condition, treatment, species, mechanism
- **matrix structure**: one row label column plus many numeric columns
- **replicate structure**: repeated observations within each category or condition

## Step 2: Match the analytical goal

Common intents:
- compare categories
- show a trend over a continuous variable
- compare several metrics over the same x-axis
- show raw variability / uncertainty / distribution
- show pairwise similarity or a full matrix
- show a relationship between two measured variables

## Step 3: Recommended defaults

### Grouped bar
Choose this when:
- categories are discrete
- values are already aggregated
- there are 2-6 series per category
- the main question is comparison, not distribution

Typical patterns:
- one categorical column + several numeric series columns
- or long-format `(group, category, value)` data with one value per combination

### Boxplot or violin
Choose this when:
- there are repeated observations per category
- the user wants a fair comparison across treatments or groups
- showing spread matters more than only showing means

Default choice:
- start with **boxplot** for clean scientific comparison
- prefer **violin** only when the shape of the distribution is part of the story

### Line chart
Choose this when:
- x is continuous or ordered
- the plot should show a profile, trend, scan, or trajectory
- each group forms a meaningful ordered series

Use **log scale** when:
- the response spans orders of magnitude
- positive values vary by roughly 100× or more

Use an **inset** when:
- a scientifically important early/low-magnitude region would otherwise disappear

### Multi-panel line figure
Choose this when:
- there are 2+ response variables that share the same x-axis
- stacking or faceting panels is clearer than overlaying everything
- the user wants a paper-style figure with one metric per panel

Good default:
- two vertically stacked panels for two response variables over the same x-axis

### Scatter
Choose this when:
- the important thing is the relationship between points, not a continuous trend line
- x is not naturally an ordered progression, or observations are sparse
- the user is comparing measured observations across groups

Use **bubble scatter** only when marker size carries real meaning.

### Heatmap
Choose this when:
- the data is fundamentally a matrix
- there is one row-label column and many numeric columns
- row/column structure matters as much as the values
- the user mentions correlation, similarity, sensitivity matrix, or pairwise comparison

## When to ask a clarifying question

Ask one concise question only if:
- there are several equally plausible y-variables and choosing one would change the plot meaning
- the dataset is too messy to infer a trustworthy x variable or measure variable
- the user expects a real plot but the provided file is missing or unreadable
- the user explicitly asks for a comparison between two possible visual stories

## When not to ask

Do **not** ask the user to choose between line vs scatter, bar vs boxplot, or one-panel vs two-panel if the data profile makes one option clearly more scientific.

Choose a strong default and move forward.

## After choosing the family

Before opening many raw references, read the distilled pattern notes under `../../patterns/` when they exist.
This is especially important for crowded families like `line` and `multi_panel`, where the repository intentionally keeps only a few canonical starters plus a handful of variants.

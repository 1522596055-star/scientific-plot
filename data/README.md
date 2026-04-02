# data

This directory stores reusable datasets for plotting samples.

## Structure

- `shared/` — reusable synthetic datasets used across multiple samples

## Rule

If a new sample can be created from an existing shared dataset, reuse it.
Only create a new shared dataset when the current ones cannot support the new chart family cleanly.

# skills

Bundled agent skills for this repository.

## Available skills
- `scientific-plotter/` — profiles raw scientific data, chooses a chart family when needed, searches the local plotting template library, and produces both `plot.py` and `output.png`

## Intended usage
Point your agent harness at this `skills/` directory, or directly at `skills/scientific-plotter/` if it expects a single skill path.

For Pi, add this directory to `~/.pi/settings.json`:

```json
{
  "skills": [
    "/path/to/scientific-plot/skills"
  ]
}
```

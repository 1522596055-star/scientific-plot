from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
DATA_PATH = ROOT / "data" / "shared" / "profile_series_v1.csv"
OUTPUT_PATH = Path(__file__).resolve().parent / "output.png"

PANEL_ORDER = ["a", "b", "c"]
PANEL_SERIES_ORDER = {
    "a": ["exp_li", "present_model", "mech_a", "mech_b", "mech_c"],
    "b": ["exp_4_1", "exp_3_2", "present_4_1", "baseline_4_1", "present_3_2", "baseline_3_2"],
    "c": ["exp_4_1", "exp_3_2", "present_4_1", "baseline_4_1", "present_3_2", "baseline_3_2"],
}
PANEL_CONFIG = {
    "a": {"title": "(a) mechanism comparison", "tag": "CH4/NH3/O2/N2, phi=0.9", "x_lim": (-0.2, 20.0), "y_lim": (0.0, 5500.0)},
    "b": {"title": "(b) O2/N2 = 0.21 / 0.79", "tag": "phi=0.9", "x_lim": (-0.2, 16.0), "y_lim": (0.0, 5000.0)},
    "c": {"title": "(c) O2/N2 = 0.35 / 0.65", "tag": "phi=0.9", "x_lim": (-0.2, 16.0), "y_lim": (0.0, 7000.0)},
}
SERIES_STYLE = {
    "exp_li": {"kind": "point", "label": "experiment", "color": "#111111", "marker": "o", "fill": "none"},
    "present_model": {"kind": "line", "label": "present", "color": "#c2471a", "linestyle": "-"},
    "mech_a": {"kind": "line", "label": "mech A", "color": "#111111", "linestyle": ":"},
    "mech_b": {"kind": "line", "label": "mech B", "color": "#78b8c5", "linestyle": "-."},
    "mech_c": {"kind": "line", "label": "mech C", "color": "#7b238b", "linestyle": "--"},
    "exp_4_1": {"kind": "point", "label": "exp 4:1", "color": "#111111", "marker": "o", "fill": "none"},
    "exp_3_2": {"kind": "point", "label": "exp 3:2", "color": "#c44116", "marker": "<", "fill": "none"},
    "present_4_1": {"kind": "line", "label": "model 4:1", "color": "#111111", "linestyle": "-"},
    "baseline_4_1": {"kind": "line", "label": "_nolegend_", "color": "#111111", "linestyle": "--"},
    "present_3_2": {"kind": "line", "label": "model 3:2", "color": "#c44116", "linestyle": "-"},
    "baseline_3_2": {"kind": "line", "label": "_nolegend_", "color": "#c44116", "linestyle": ":"},
}


def load_profiles():
    grouped = defaultdict(lambda: defaultdict(list))
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row["figure_group"] != "combustion_no_profiles":
                continue
            grouped[row["panel_id"]][row["series_id"]].append((float(row["x_value"]), float(row["y_value"])))

    for panel_id in grouped:
        for series_id in grouped[panel_id]:
            grouped[panel_id][series_id].sort(key=lambda item: item[0])
    return grouped


def plot_series(ax: plt.Axes, xs, ys, style):
    if style["kind"] == "point":
        markerfacecolor = "white" if style.get("fill") == "none" else style["color"]
        ax.plot(
            xs,
            ys,
            linestyle="None",
            marker=style["marker"],
            markersize=6.0,
            markerfacecolor=markerfacecolor,
            markeredgecolor=style["color"],
            markeredgewidth=1.4,
            color=style["color"],
            label=style["label"],
        )
    else:
        ax.plot(xs, ys, color=style["color"], linestyle=style["linestyle"], linewidth=1.8, label=style["label"])


def main() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Serif",
            "axes.linewidth": 1.2,
            "xtick.major.width": 1.0,
            "ytick.major.width": 1.0,
        }
    )

    grouped = load_profiles()
    fig, axes = plt.subplots(1, 3, figsize=(16, 4.6), dpi=180)

    for ax, panel_id in zip(axes, PANEL_ORDER):
        for series_id in PANEL_SERIES_ORDER[panel_id]:
            points = grouped[panel_id][series_id]
            xs = [point[0] for point in points]
            ys = [point[1] for point in points]
            plot_series(ax, xs, ys, SERIES_STYLE[series_id])

        config = PANEL_CONFIG[panel_id]
        ax.set_xlim(*config["x_lim"])
        ax.set_ylim(*config["y_lim"])
        ax.set_xlabel("Height above burner (mm)", fontsize=12)
        ax.set_ylabel("NO mole fraction (ppm)", fontsize=12)
        ax.tick_params(labelsize=10)
        ax.text(0.04, 0.95, config["title"], transform=ax.transAxes, fontsize=12, fontweight="bold", va="top")
        ax.text(0.04, 0.86, config["tag"], transform=ax.transAxes, fontsize=11, va="top")
        ax.legend(frameon=False, fontsize=9, loc="lower right")

    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

ROOT = Path(__file__).resolve().parents[3]
DATA_PATH = ROOT / "data" / "shared" / "profile_series_v1.csv"
OUTPUT_PATH = Path(__file__).resolve().parent / "output.png"

PANEL_ORDER = ["a", "b", "c"]
PANEL_CONFIG = {
    "a": {"title": "(a) Z/D = 1", "y_lim": (0, 2300)},
    "b": {"title": "(b) Z/D = 4", "y_lim": (0, 2300)},
    "c": {"title": "(c) Z/D = 10", "y_lim": (0, 2300)},
}
STYLE = {
    "sim_mean": {"kind": "line", "color": "#111111", "linestyle": "-", "linewidth": 2.0, "label": "sim. mean"},
    "sim_rms": {"kind": "line", "color": "#d9485f", "linestyle": "--", "linewidth": 1.8, "label": "sim. rms"},
    "exp_mean": {"kind": "point", "color": "#111111", "marker": "o", "fill": "full", "label": "ref. mean"},
    "exp_rms": {"kind": "point", "color": "#111111", "marker": "o", "fill": "none", "label": "ref. rms"},
}
SERIES_ORDER = ["sim_mean", "sim_rms", "exp_mean", "exp_rms"]


def load_profiles():
    grouped = defaultdict(lambda: defaultdict(list))
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row["figure_group"] != "mixture_fraction_temperature_profiles":
                continue
            grouped[row["panel_id"]][row["series_id"]].append((float(row["x_value"]), float(row["y_value"])))
    for panel_id in grouped:
        for series_id in grouped[panel_id]:
            grouped[panel_id][series_id].sort(key=lambda item: item[0])
    return grouped


def plot_series(ax, xs, ys, style):
    if style["kind"] == "line":
        ax.plot(xs, ys, color=style["color"], linestyle=style["linestyle"], linewidth=style["linewidth"], label=style["label"])
        return

    markerfacecolor = style["color"] if style.get("fill") == "full" else "white"
    ax.plot(
        xs,
        ys,
        linestyle="None",
        marker=style["marker"],
        markersize=4.6,
        markerfacecolor=markerfacecolor,
        markeredgecolor=style["color"],
        markeredgewidth=0.9,
        color=style["color"],
        label=style["label"],
    )


def main() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Serif",
            "mathtext.fontset": "stix",
            "axes.linewidth": 1.0,
            "xtick.major.width": 0.9,
            "ytick.major.width": 0.9,
        }
    )

    grouped = load_profiles()
    fig, axes = plt.subplots(1, 3, figsize=(13.2, 4.1), dpi=180)

    for ax, panel_id in zip(axes, PANEL_ORDER):
        for series_id in SERIES_ORDER:
            points = grouped[panel_id][series_id]
            xs = [point[0] for point in points]
            ys = [point[1] for point in points]
            plot_series(ax, xs, ys, STYLE[series_id])

        config = PANEL_CONFIG[panel_id]
        ax.set_xlim(0.0, 1.0)
        ax.set_ylim(*config["y_lim"])
        ax.set_xlabel("ξ [-]", fontsize=11)
        ax.set_ylabel("T [K]", fontsize=11)
        ax.tick_params(labelsize=9)
        ax.grid(alpha=0.22, linewidth=0.8)
        ax.text(0.05, 0.95, config["title"], transform=ax.transAxes, ha="left", va="top", fontsize=12, fontweight="bold")

    legend_handles = [
        Line2D([0], [0], color="#111111", linewidth=2.0, label="sim. mean"),
        Line2D([0], [0], color="#d9485f", linewidth=1.8, linestyle="--", label="sim. rms"),
        Line2D([0], [0], marker="o", color="#111111", markerfacecolor="#111111", markersize=5.5, linestyle="None", label="ref. mean"),
        Line2D([0], [0], marker="o", color="#111111", markerfacecolor="white", markersize=5.5, linestyle="None", label="ref. rms"),
    ]
    fig.legend(handles=legend_handles, loc="upper center", ncol=4, frameon=False, fontsize=10, bbox_to_anchor=(0.5, 1.02))

    fig.tight_layout(rect=(0, 0, 1, 0.93))
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()

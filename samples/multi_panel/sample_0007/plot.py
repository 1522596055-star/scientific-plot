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

PANELS = ["left", "right"]
PANEL_CONFIG = {
    "left": {"title": "(a) Temperature", "x_lim": (0.015, 0.027), "y_lim": (200, 1700), "y_label": "T [K]"},
    "right": {"title": "(b) Interstitial velocity", "x_lim": (0.017, 0.031), "y_lim": (0.5, 6.2), "y_label": r"u$_i$ [m s$^{-1}$]"},
}
STYLE = {
    "reference": {"kind": "point", "color": "#111111", "marker": "o", "label": "reference"},
    "vas": {"kind": "line", "color": "#d9485f", "linestyle": "-", "linewidth": 2.0, "label": "VAS model"},
}
SERIES_ORDER = ["reference", "vas"]


def load_profiles():
    grouped = defaultdict(lambda: defaultdict(list))
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row["figure_group"] != "porous_media_validation_pair":
                continue
            grouped[row["panel_id"]][row["series_id"]].append((float(row["x_value"]), float(row["y_value"])))
    for panel_id in grouped:
        for series_id in grouped[panel_id]:
            grouped[panel_id][series_id].sort(key=lambda item: item[0])
    return grouped


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
    fig, axes = plt.subplots(1, 2, figsize=(9.8, 4.2), dpi=180)

    for ax, panel_id in zip(axes, PANELS):
        for series_id in SERIES_ORDER:
            points = grouped[panel_id][series_id]
            xs = [point[0] for point in points]
            ys = [point[1] for point in points]
            style = STYLE[series_id]
            if style["kind"] == "line":
                ax.plot(xs, ys, color=style["color"], linestyle=style["linestyle"], linewidth=style["linewidth"], label=style["label"])
            else:
                ax.plot(
                    xs,
                    ys,
                    linestyle="None",
                    marker=style["marker"],
                    markersize=4.5,
                    markerfacecolor="white",
                    markeredgecolor=style["color"],
                    markeredgewidth=0.9,
                    color=style["color"],
                    label=style["label"],
                )

        config = PANEL_CONFIG[panel_id]
        ax.set_xlim(*config["x_lim"])
        ax.set_ylim(*config["y_lim"])
        ax.set_xlabel("x [m]", fontsize=11)
        ax.set_ylabel(config["y_label"], fontsize=11)
        ax.tick_params(labelsize=9)
        ax.grid(alpha=0.22, linewidth=0.8)
        ax.text(0.05, 0.95, config["title"], transform=ax.transAxes, ha="left", va="top", fontsize=12, fontweight="bold")

    legend_handles = [
        Line2D([0], [0], marker="o", color="#111111", markerfacecolor="white", markersize=5.5, linestyle="None", label="reference"),
        Line2D([0], [0], color="#d9485f", linewidth=2.0, label="VAS model"),
    ]
    fig.legend(handles=legend_handles, loc="upper center", ncol=2, frameon=False, fontsize=10, bbox_to_anchor=(0.5, 1.01))

    fig.tight_layout(rect=(0, 0, 1, 0.92))
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()

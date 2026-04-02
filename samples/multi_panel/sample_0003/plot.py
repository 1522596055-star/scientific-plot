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

PANEL_ORDER = ["a", "b", "c", "d", "e", "f"]
PANEL_TITLES = {
    "a": r"(a) C$_2$H$_4$",
    "b": r"(b) CH$_2$O",
    "c": r"(c) CH$_3$OH",
    "d": r"(d) CH$_3$CHO",
    "e": r"(e) CH$_4$",
    "f": r"(f) COC*C",
}
PANEL_LIMITS = {
    "a": {"x_lim": (725, 1075), "y_lim": (-0.25, 1.75), "y_ticks": [0.0, 0.5, 1.0, 1.5]},
    "b": {"x_lim": (725, 1075), "y_lim": (-0.25, 1.75), "y_ticks": [0.0, 0.5, 1.0, 1.5]},
    "c": {"x_lim": (725, 1075), "y_lim": (-0.10, 0.39), "y_ticks": [0.0, 0.12, 0.24, 0.36]},
    "d": {"x_lim": (725, 1075), "y_lim": (-0.02, 0.13), "y_ticks": [0.0, 0.04, 0.08, 0.12]},
    "e": {"x_lim": (725, 1075), "y_lim": (-0.10, 0.52), "y_ticks": [0.0, 0.16, 0.32, 0.48]},
    "f": {"x_lim": (700, 1100), "y_lim": (-0.10, 0.52), "y_ticks": [0.0, 0.16, 0.32, 0.48]},
}
EXP_STYLE = {"color": "#72c5c3", "marker": "s"}
SIM_STYLE = {"color": "#e84a8b"}


def load_data():
    grouped = defaultdict(lambda: {"line": [], "point": []})

    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row["figure_group"] != "temperature_species_profiles":
                continue
            grouped[row["panel_id"]][row["series_type"]].append(
                {
                    "x": float(row["x_value"]),
                    "y": float(row["y_value"]),
                    "err_low": float(row["error_low"]),
                    "err_high": float(row["error_high"]),
                }
            )

    for panel_id in grouped:
        grouped[panel_id]["line"].sort(key=lambda item: item["x"])
        grouped[panel_id]["point"].sort(key=lambda item: item["x"])
    return grouped


def main() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Serif",
            "mathtext.fontset": "stix",
            "axes.linewidth": 1.1,
            "xtick.major.width": 0.9,
            "ytick.major.width": 0.9,
        }
    )

    grouped = load_data()
    fig, axes = plt.subplots(2, 3, figsize=(14, 8), dpi=180)

    for ax, panel_id in zip(axes.flat, PANEL_ORDER):
        line_points = grouped[panel_id]["line"]
        point_series = grouped[panel_id]["point"]

        line_x = [point["x"] for point in line_points]
        line_y = [point["y"] for point in line_points]
        point_x = [point["x"] for point in point_series]
        point_y = [point["y"] for point in point_series]
        point_yerr = [
            [point["err_low"] for point in point_series],
            [point["err_high"] for point in point_series],
        ]

        ax.plot(line_x, line_y, color=SIM_STYLE["color"], linewidth=2.8, solid_capstyle="round")
        ax.errorbar(
            point_x,
            point_y,
            yerr=point_yerr,
            fmt=EXP_STYLE["marker"],
            markersize=6.8,
            color=EXP_STYLE["color"],
            ecolor=EXP_STYLE["color"],
            markerfacecolor=EXP_STYLE["color"],
            markeredgecolor=EXP_STYLE["color"],
            elinewidth=3.0,
            capsize=5.0,
            capthick=2.2,
            linestyle="None",
        )

        limits = PANEL_LIMITS[panel_id]
        ax.set_xlim(*limits["x_lim"])
        ax.set_ylim(*limits["y_lim"])
        ax.set_yticks(limits["y_ticks"])
        if panel_id == "f":
            ax.set_xticks(list(range(700, 1101, 50)))
        else:
            ax.set_xticks(list(range(750, 1051, 50)))
        ax.set_xlabel("Temperature (K)", fontsize=16)
        ax.set_ylabel(r"Mole fraction ($10^{-3}$)", fontsize=16)
        ax.tick_params(labelsize=11)
        ax.text(0.03, 0.95, PANEL_TITLES[panel_id], transform=ax.transAxes, ha="left", va="top", fontsize=17, fontweight="bold")

    legend_handles = [
        Line2D([0], [0], marker="s", color="none", markerfacecolor=EXP_STYLE["color"], markeredgecolor=EXP_STYLE["color"], markersize=10, label="Experiment"),
        Line2D([0], [0], color=SIM_STYLE["color"], linewidth=3.0, solid_capstyle="round", label="Simulation"),
    ]
    axes[0, 0].legend(handles=legend_handles, frameon=False, loc="upper right", fontsize=14, handlelength=2.6, handletextpad=0.5)

    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()

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
PANEL_META = {
    "a": {"title": r"(a) Y$_{\mathrm{O_2}}$", "y_label": r"Y$_{\mathrm{O_2}}$ [-]", "y_lim": (0.0, 0.24)},
    "b": {"title": r"(b) Y$_{\mathrm{H_2O}}$", "y_label": r"Y$_{\mathrm{H_2O}}$ [-]", "y_lim": (0.0, 0.14)},
    "c": {"title": r"(c) T", "y_label": "T [K]", "y_lim": (0.0, 2600.0)},
    "d": {"title": r"(d) Y$_{\mathrm{CO}}$", "y_label": r"Y$_{\mathrm{CO}}$ [-]", "y_lim": (0.0, 0.14)},
    "e": {"title": r"(e) Y$_{\mathrm{HCN}}$", "y_label": r"Y$_{\mathrm{HCN}}$ [-]", "y_lim": (0.0, 0.03)},
    "f": {"title": r"(f) Y$_{\mathrm{NO}}$", "y_label": r"Y$_{\mathrm{NO}}$ [-]", "y_lim": (0.0, 0.006)},
}
REFERENCE_STYLE = {"color": "#1f1f1f", "marker": "o"}
MODEL_STYLE = {"color": "#d9485f"}
ZONE_SPANS = [(1.5, 2.4, "#e8c3cb"), (6.6, 10.4, "#b8dfd5")]


def load_data():
    grouped = defaultdict(lambda: {"line": [], "point": []})
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row["figure_group"] != "flamelet_validation_profiles":
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
            "axes.linewidth": 1.0,
            "xtick.major.width": 0.9,
            "ytick.major.width": 0.9,
        }
    )

    grouped = load_data()
    fig, axes = plt.subplots(2, 3, figsize=(14, 8.8), dpi=180)

    for ax, panel_id in zip(axes.flat, PANEL_ORDER):
        panel = grouped[panel_id]
        line_x = [item["x"] for item in panel["line"]]
        line_y = [item["y"] for item in panel["line"]]
        point_x = [item["x"] for item in panel["point"]]
        point_y = [item["y"] for item in panel["point"]]
        point_yerr = [
            [item["err_low"] for item in panel["point"]],
            [item["err_high"] for item in panel["point"]],
        ]

        for xmin, xmax, color in ZONE_SPANS:
            ax.axvspan(xmin, xmax, color=color, alpha=0.45, lw=0)

        ax.plot(line_x, line_y, color=MODEL_STYLE["color"], linewidth=2.1, label="Flamelet model")
        ax.errorbar(
            point_x,
            point_y,
            yerr=point_yerr,
            fmt=REFERENCE_STYLE["marker"],
            markersize=4.5,
            markerfacecolor="white",
            markeredgecolor=REFERENCE_STYLE["color"],
            markeredgewidth=0.9,
            color=REFERENCE_STYLE["color"],
            ecolor=REFERENCE_STYLE["color"],
            elinewidth=0.8,
            capsize=0,
            linestyle="None",
            label="Reference",
        )

        meta = PANEL_META[panel_id]
        ax.set_xlim(0, 20)
        ax.set_ylim(*meta["y_lim"])
        ax.set_xlabel("y [mm]", fontsize=11)
        ax.set_ylabel(meta["y_label"], fontsize=11)
        ax.tick_params(labelsize=9)
        ax.grid(alpha=0.22, linewidth=0.8)
        ax.text(0.03, 0.95, meta["title"], transform=ax.transAxes, ha="left", va="top", fontsize=14, fontweight="bold")

    legend_handles = [
        Line2D([0], [0], marker="o", color=REFERENCE_STYLE["color"], markerfacecolor="white", markeredgecolor=REFERENCE_STYLE["color"], markersize=6, linestyle="None", label="Reference"),
        Line2D([0], [0], color=MODEL_STYLE["color"], linewidth=2.1, label="Flamelet model"),
    ]
    fig.legend(handles=legend_handles, frameon=False, loc="upper center", ncol=2, fontsize=11, bbox_to_anchor=(0.5, 0.985))

    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()

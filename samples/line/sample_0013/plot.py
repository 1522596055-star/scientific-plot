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

SERIES_ORDER = ["detailed", "gpc_25", "lpc_23_k2", "lpc_18_k3", "lpc_12_k4"]
STYLE = {
    "detailed": {"color": "#111111", "linestyle": "-", "linewidth": 2.0, "label": "detailed chemistry"},
    "gpc_25": {"color": "#d9485f", "linestyle": "--", "linewidth": 1.8, "label": "G-PC 25"},
    "lpc_23_k2": {"color": "#6f6f6f", "linestyle": ":", "linewidth": 1.9, "label": "L-PC 23 · k=2"},
    "lpc_18_k3": {"color": "#c75fd6", "linestyle": "-.", "linewidth": 1.7, "label": "L-PC 18 · k=3"},
    "lpc_12_k4": {"color": "#3f60ff", "linestyle": (0, (5, 2, 1, 2)), "linewidth": 1.7, "label": "L-PC 12 · k=4"},
}


def load_profiles():
    grouped = defaultdict(list)
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row["figure_group"] != "reduced_order_temperature_solutions":
                continue
            grouped[row["series_id"]].append((float(row["x_value"]), float(row["y_value"])))
    for series_id in grouped:
        grouped[series_id].sort(key=lambda item: item[0])
    return grouped


def main() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Serif",
            "axes.linewidth": 1.1,
            "xtick.major.width": 0.9,
            "ytick.major.width": 0.9,
        }
    )

    grouped = load_profiles()
    fig, ax = plt.subplots(figsize=(5.0, 4.2), dpi=180)

    for series_id in SERIES_ORDER:
        points = grouped[series_id]
        style = STYLE[series_id]
        ax.plot(
            [point[0] for point in points],
            [point[1] for point in points],
            color=style["color"],
            linestyle=style["linestyle"],
            linewidth=style["linewidth"],
            label=style["label"],
        )

    ax.set_xlim(0.0, 0.010)
    ax.set_ylim(1400, 2750)
    ax.set_xlabel("time [s]", fontsize=11)
    ax.set_ylabel("T [K]", fontsize=11)
    ax.tick_params(labelsize=9)
    ax.grid(alpha=0.22, linewidth=0.8)
    ax.legend(frameon=False, fontsize=8.5, loc="upper left")

    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()

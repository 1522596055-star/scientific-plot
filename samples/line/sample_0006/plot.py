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

SERIES_ORDER = ["burner_stabilized", "le_1_4", "le_1_2", "le_0_8_stable", "le_0_8_unstable"]
SERIES_STYLE = {
    "burner_stabilized": {"color": "#111111", "linestyle": ":", "linewidth": 1.8, "label": "burner stabilized"},
    "le_1_4": {"color": "#2d43ff", "linestyle": "-", "linewidth": 1.8, "label": "Le = 1.4"},
    "le_1_2": {"color": "#1a9c2c", "linestyle": "-", "linewidth": 1.8, "label": "Le = 1.2"},
    "le_0_8_stable": {"color": "#ff2a2a", "linestyle": "-", "linewidth": 1.8, "label": "Le = 0.8"},
    "le_0_8_unstable": {"color": "#ff2a2a", "linestyle": ":", "linewidth": 1.8, "label": "_nolegend_"},
}


def load_series():
    grouped = defaultdict(list)
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row["figure_group"] != "flame_coordinate_vs_flow":
                continue
            grouped[row["series_id"]].append((float(row["x_value"]), float(row["y_value"])))

    for series_id in grouped:
        grouped[series_id].sort(key=lambda item: item[0])
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

    grouped = load_series()
    fig, ax = plt.subplots(figsize=(5.0, 4.6), dpi=180)

    for series_id in SERIES_ORDER:
        xs = [point[0] for point in grouped[series_id]]
        ys = [point[1] for point in grouped[series_id]]
        style = SERIES_STYLE[series_id]
        ax.plot(xs, ys, color=style["color"], linestyle=style["linestyle"], linewidth=style["linewidth"], label=style["label"])

    ax.set_xlim(0.0, 1.2)
    ax.set_ylim(0.0, 15.0)
    ax.set_xticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2])
    ax.set_yticks([0, 5, 10, 15])
    ax.set_xlabel(r"$V_0$", fontsize=16)
    ax.set_ylabel(r"$x_{FS}$", fontsize=16)
    ax.tick_params(labelsize=10, direction="in", top=True, right=True)
    ax.legend(frameon=False, fontsize=9, loc="upper left")

    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()

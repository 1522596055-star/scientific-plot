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
STYLE = {
    "md_ce": ("#30d44f", "o", "Methanol/Diesel RCCI"),
    "ad_ce": ("#3255ff", "o", "Ammonia/Diesel RCCI"),
    "md_ite": ("#30d44f", "o", "Methanol/Diesel RCCI"),
    "ad_ite": ("#3255ff", "o", "Ammonia/Diesel RCCI"),
}
PANEL_CONFIG = [
    ("top", "Combustion Efficiency [%]", (60, 100)),
    ("bottom", "Gross ITE [%]", (30, 55)),
]


def configure_matplotlib() -> None:
    plt.rcParams.update({"font.family": "DejaVu Serif"})


def load_series() -> dict[str, dict[str, list[tuple[float, float]]]]:
    grouped: dict[str, dict[str, list[tuple[float, float]]]] = defaultdict(lambda: defaultdict(list))
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["figure_group"] != "rcci_efficiency":
                continue
            grouped[row["panel_id"]][row["series_id"]].append((float(row["x_value"]), float(row["y_value"])))

    for panel_data in grouped.values():
        for points in panel_data.values():
            points.sort(key=lambda item: item[0])
    return grouped


def plot_panel(
    ax: plt.Axes,
    panel_id: str,
    ylabel: str,
    ylim: tuple[float, float],
    series_data: dict[str, list[tuple[float, float]]],
) -> None:
    for series_id, points in series_data.items():
        color, marker, label = STYLE[series_id]
        xs = [x for x, _ in points]
        ys = [y for _, y in points]
        ax.plot(
            xs,
            ys,
            color=color,
            marker=marker,
            markersize=3.5,
            linewidth=1.2,
            markerfacecolor="white",
            label=label,
        )

    ax.set_xlim(0.0, 0.8)
    ax.set_ylim(*ylim)
    ax.set_xlabel("Premixed Energy Ratio", fontsize=11)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.tick_params(labelsize=8)
    ax.legend(frameon=False, fontsize=7, loc="lower left")


def main() -> None:
    configure_matplotlib()
    grouped = load_series()

    fig, axes = plt.subplots(2, 1, figsize=(4.5, 8.2), dpi=180)
    for ax, (panel_id, ylabel, ylim) in zip(axes, PANEL_CONFIG):
        plot_panel(ax, panel_id, ylabel, ylim, grouped[panel_id])

    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")


if __name__ == "__main__":
    main()

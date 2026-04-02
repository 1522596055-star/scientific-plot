from __future__ import annotations

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

ROOT = Path(__file__).resolve().parents[3]
DATA_PATH = ROOT / "data" / "shared" / "profile_series_v1.csv"
OUTPUT_PATH = Path(__file__).resolve().parent / "output.png"

SERIES_ORDER = ["heat_base", "heat_no_1pct", "heat_no_10_4pct"]
SERIES_STYLE = {
    "heat_base": {"label": "Base Mixture", "color": "#000000", "linestyle": "-", "linewidth": 2.2},
    "heat_no_1pct": {"label": "NO 1%", "color": "#ff0000", "linestyle": "-", "linewidth": 2.2},
    "heat_no_10_4pct": {"label": "NO 10.4%", "color": "#1f34ff", "linestyle": "-", "linewidth": 2.2},
}
TOP_TICKS = [3.5, 4.0, 4.5, 5.0, 5.5]
TOP_LABELS = ["939", "1033", "1139", "1261", "1350"]


def load_series():
    grouped = {series_id: [] for series_id in SERIES_ORDER}
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row["figure_group"] != "heat_release_profiles":
                continue
            grouped[row["series_id"]].append((float(row["x_value"]), float(row["y_value"])))

    for series_id in grouped:
        grouped[series_id].sort(key=lambda item: item[0])
    return grouped


def add_secondary_temperature_axis(ax: plt.Axes, ticks, labels, label_size: int) -> None:
    secondary = ax.secondary_xaxis("top")
    secondary.set_xticks(ticks)
    secondary.set_xticklabels(labels)
    secondary.set_xlabel(r"$T_w$ [K]", fontsize=label_size, fontweight="bold")
    secondary.tick_params(axis="x", labelsize=label_size - 2, width=1.0, length=4)


def draw_curves(ax: plt.Axes, grouped) -> None:
    for series_id in SERIES_ORDER:
        xs = [point[0] for point in grouped[series_id]]
        ys = [point[1] for point in grouped[series_id]]
        style = SERIES_STYLE[series_id]
        ax.plot(xs, ys, color=style["color"], linestyle=style["linestyle"], linewidth=style["linewidth"], label=style["label"], solid_capstyle="round")


def main() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "axes.linewidth": 1.4,
            "xtick.major.width": 1.1,
            "ytick.major.width": 1.1,
        }
    )

    grouped = load_series()
    fig, ax = plt.subplots(figsize=(9.2, 6.8), dpi=180)

    draw_curves(ax, grouped)
    ax.set_xlim(3.5, 5.5)
    ax.set_ylim(0, 45)
    ax.set_xticks([3.5, 4.0, 4.5, 5.0, 5.5])
    ax.set_yticks([0, 9, 18, 27, 36, 45])
    ax.set_xlabel("x [cm]", fontsize=20, fontweight="bold")
    ax.set_ylabel(r"Heat Release Rate [W/cm$^3$]", fontsize=20, fontweight="bold")
    ax.tick_params(labelsize=13, length=6)
    ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.52, 1.02), fontsize=16, handlelength=2.6, handletextpad=0.5)
    ax.text(0.01, 0.94, r"$T_{w,\max}=1400\ \mathrm{K}$", transform=ax.transAxes, ha="left", va="center", fontsize=18, fontweight="bold")
    add_secondary_temperature_axis(ax, TOP_TICKS, TOP_LABELS, 18)

    inset_ax = inset_axes(ax, width="35%", height="28%", loc="lower left", borderpad=3.0)
    draw_curves(inset_ax, grouped)
    inset_ax.set_xlim(3.5, 4.5)
    inset_ax.set_ylim(0, 2.4)
    inset_ax.set_xticks([3.5, 4.0, 4.5])
    inset_ax.set_yticks([0.0, 0.6, 1.2, 1.8, 2.4])
    inset_ax.set_xlabel("x [cm]", fontsize=11)
    inset_ax.tick_params(labelsize=10, length=4)
    add_secondary_temperature_axis(inset_ax, [3.5, 4.0, 4.5], ["939", "1033", "1139"], 11)
    ax.indicate_inset_zoom(inset_ax, edgecolor="#ff4aa2", linewidth=1.5, alpha=1.0)

    fig.subplots_adjust(left=0.12, right=0.98, bottom=0.13, top=0.88)
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()

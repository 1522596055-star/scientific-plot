from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

ROOT = Path(__file__).resolve().parents[3]
DATA_PATH = ROOT / "data" / "shared" / "profile_series_v1.csv"
OUTPUT_PATH = Path(__file__).resolve().parent / "output.png"

SERIES_ORDER = [
    "r34_base",
    "r34_no_1pct",
    "r34_no_10_4pct",
    "r31_base",
    "r31_no_1pct",
    "r31_no_10_4pct",
    "r32_base",
    "r32_no_1pct",
    "r32_no_10_4pct",
    "r33_base",
    "r33_no_1pct",
    "r33_no_10_4pct",
]
REACTION_COLORS = {
    "r34": "#10a810",
    "r31": "#000000",
    "r32": "#ff0000",
    "r33": "#1f34ff",
}
CONDITION_LINESTYLES = {
    "base": "-",
    "no_1pct": "-.",
    "no_10_4pct": "--",
}
TOP_TICKS = [3.5, 4.0, 4.5, 5.0, 5.5]
TOP_LABELS = ["939", "1033", "1139", "1261", "1350"]


def load_series():
    grouped: dict[str, list[tuple[float, float]]] = defaultdict(list)
    style_keys: dict[str, tuple[str, str]] = {}

    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row["figure_group"] != "ch4_rate_profiles":
                continue
            series_id = row["series_id"]
            grouped[series_id].append((float(row["x_value"]), float(row["y_value"])))
            style_keys[series_id] = (row["reaction_id"], row["condition_id"])

    for series_id in grouped:
        grouped[series_id].sort(key=lambda item: item[0])
    return grouped, style_keys


def add_secondary_temperature_axis(ax: plt.Axes, ticks, labels, label_size: int) -> None:
    secondary = ax.secondary_xaxis("top")
    secondary.set_xticks(ticks)
    secondary.set_xticklabels(labels)
    secondary.set_xlabel(r"$T_w$ [K]", fontsize=label_size, fontweight="bold")
    secondary.tick_params(axis="x", labelsize=label_size - 2, width=1.0, length=4)


def plot_all_series(ax: plt.Axes, grouped, style_keys) -> None:
    for series_id in SERIES_ORDER:
        reaction_id, condition_id = style_keys[series_id]
        xs = [point[0] for point in grouped[series_id]]
        ys = [point[1] for point in grouped[series_id]]
        ax.plot(
            xs,
            ys,
            color=REACTION_COLORS[reaction_id],
            linestyle=CONDITION_LINESTYLES[condition_id],
            linewidth=2.0,
            solid_capstyle="round",
        )


def main() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "axes.linewidth": 1.4,
            "xtick.major.width": 1.1,
            "ytick.major.width": 1.1,
        }
    )

    grouped, style_keys = load_series()
    fig, ax = plt.subplots(figsize=(10.2, 7.4), dpi=180)

    plot_all_series(ax, grouped, style_keys)
    ax.set_xlim(3.5, 5.5)
    ax.set_ylim(-5.0e-5, 3.0e-5)
    ax.set_xticks([3.5, 4.0, 4.5, 5.0, 5.5])
    ax.set_yticks([-5e-5, -4e-5, -3e-5, -2e-5, -1e-5, 0.0, 1e-5, 2e-5, 3e-5])
    ax.set_yticklabels(["-5E-5", "-4E-5", "-3E-5", "-2E-5", "-1E-5", "0E+0", "1E-5", "2E-5", "3E-5"])
    ax.set_xlabel("x [cm]", fontsize=20, fontweight="bold")
    ax.set_ylabel(r"Rates of CH$_4$ Production [mol/s-cm$^3$]", fontsize=18, fontweight="bold")
    ax.tick_params(labelsize=13, length=6)
    add_secondary_temperature_axis(ax, TOP_TICKS, TOP_LABELS, 18)
    ax.text(
        0.02,
        0.96,
        r"$T_{w,\max}=1400\ \mathrm{K}$",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=16,
        fontweight="bold",
        bbox={"facecolor": "white", "edgecolor": "black", "boxstyle": "square,pad=0.2"},
    )

    condition_handles = [
        Line2D([0], [0], color="black", linewidth=2.0, linestyle="-", label="Base Mixture"),
        Line2D([0], [0], color="black", linewidth=2.0, linestyle="-.", label="NO 1%"),
        Line2D([0], [0], color="black", linewidth=2.0, linestyle="--", label="NO 10.4%"),
    ]
    reaction_handles = [
        Line2D([0], [0], color="#10a810", linewidth=2.0, label="R34"),
        Line2D([0], [0], color="#000000", linewidth=2.0, label="R31"),
        Line2D([0], [0], color="#ff0000", linewidth=2.0, label="R32"),
        Line2D([0], [0], color="#1f34ff", linewidth=2.0, label="R33"),
    ]
    condition_legend = ax.legend(handles=condition_handles, frameon=False, loc="upper left", bbox_to_anchor=(0.31, 1.02), fontsize=12, handlelength=2.8)
    ax.add_artist(condition_legend)
    ax.legend(handles=reaction_handles, frameon=False, loc="upper right", bbox_to_anchor=(0.99, 1.02), fontsize=12, handlelength=2.8)

    inset_ax = inset_axes(ax, width="34%", height="28%", loc="lower left", borderpad=3.0)
    plot_all_series(inset_ax, grouped, style_keys)
    inset_ax.set_xlim(3.5, 4.6)
    inset_ax.set_ylim(-4.2e-6, 0.2e-6)
    inset_ax.set_xticks([3.5, 4.0, 4.5])
    inset_ax.set_yticks([-4e-6, -3e-6, -2e-6, -1e-6, 0.0])
    inset_ax.set_yticklabels(["-4E-6", "-3E-6", "-2E-6", "-1E-6", "0E+0"])
    inset_ax.tick_params(labelsize=8, length=3)
    add_secondary_temperature_axis(inset_ax, [3.5, 4.0, 4.5], ["939", "1033", "1139"], 10)

    fig.subplots_adjust(left=0.12, right=0.98, bottom=0.12, top=0.90)
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()

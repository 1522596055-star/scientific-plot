from __future__ import annotations

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
DATA_PATH = ROOT / "data" / "shared" / "categorical_measurements_v1.csv"
OUTPUT_PATH = Path(__file__).resolve().parent / "output.png"

SPECIES_ORDER = ["NO", "HNO", "OH", "O", "H", "O2", "NH2", "NH", "N"]
SPECIES_LABELS = {
    "NO": "NO",
    "HNO": "HNO",
    "OH": "OH",
    "O": "O",
    "H": "H",
    "O2": r"O$_2$",
    "NH2": r"NH$_2$",
    "NH": "NH",
    "N": "N",
}
PHI_ORDER = ["0.8", "1.4"]
COLORS = {
    "0.8": "#6E51A3",
    "1.4": "#53B685",
}


def load_grouped_bar_data() -> tuple[dict[str, dict[str, float]], dict[str, int]]:
    grouped_values = {phi: {} for phi in PHI_ORDER}
    scale_powers: dict[str, int] = {}

    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            phi = row["condition_id"]
            species = row["category_id"]
            if phi not in PHI_ORDER or species not in SPECIES_ORDER:
                continue
            grouped_values[phi][species] = float(row["mean_value"])
            scale_powers[species] = int(row["scale_power"])

    return grouped_values, scale_powers


def build_tick_labels(scale_powers: dict[str, int]) -> list[str]:
    labels = []
    for species in SPECIES_ORDER:
        pretty_species = SPECIES_LABELS[species]
        labels.append(f"{pretty_species}\n($\\times 10^{{{scale_powers[species]}}}$)")
    return labels


def add_value_labels(ax: plt.Axes, bars, values: list[float]) -> None:
    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.05,
            f"{value:.2f}",
            ha="center",
            va="bottom",
            fontsize=10,
        )


def main() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Serif",
            "mathtext.fontset": "stix",
            "axes.linewidth": 1.5,
            "xtick.major.width": 1.2,
            "ytick.major.width": 1.2,
        }
    )

    grouped_values, scale_powers = load_grouped_bar_data()
    x = np.arange(len(SPECIES_ORDER))
    width = 0.35

    fig, ax = plt.subplots(figsize=(11, 7), dpi=180)

    phi_08_values = [grouped_values["0.8"][species] for species in SPECIES_ORDER]
    phi_14_values = [grouped_values["1.4"][species] for species in SPECIES_ORDER]

    bars_08 = ax.bar(x - width / 2, phi_08_values, width=width, color=COLORS["0.8"], label="phi = 0.8")
    bars_14 = ax.bar(x + width / 2, phi_14_values, width=width, color=COLORS["1.4"], label="phi = 1.4")

    add_value_labels(ax, bars_08, phi_08_values)
    add_value_labels(ax, bars_14, phi_14_values)

    ax.set_ylabel(r"Integrated mole fractions (m$^3$)", fontsize=18)
    ax.set_xticks(x)
    ax.set_xticklabels(build_tick_labels(scale_powers), fontsize=11)
    ax.set_ylim(0, 4.0)
    ax.set_xlim(-0.5, len(SPECIES_ORDER) - 0.5)
    ax.tick_params(axis="y", labelsize=12)
    ax.legend(frameon=False, loc="upper right", fontsize=13)

    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()

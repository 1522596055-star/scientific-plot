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
    "nh3_lpilot": ("#111111", "^", "L-pilot NH3"),
    "nh3_epilot": ("#e33", "o", "E-pilot NH3"),
    "nox_lpilot": ("#111111", "^", "L-pilot NOx"),
    "nox_epilot": ("#e33", "o", "E-pilot NOx"),
    "cdc_nox": ("#4477ff", None, "CDC (NOx)"),
    "n2o_lpilot": ("#111111", "^", "L-pilot N2O"),
    "n2o_epilot": ("#e33", "o", "E-pilot N2O"),
    "cdc_n2o": ("#4477ff", None, "CDC (N2O)"),
}
PANEL_CONFIG = {
    "left": {"ylabel": "NH3 / NOx [ppm]", "ylim": (0, 12000)},
    "right": {"ylabel": "N2O [ppm]", "ylim": (0, 60)},
}


def configure_matplotlib() -> None:
    plt.rcParams.update({"font.family": "DejaVu Serif"})


def load_series() -> dict[str, dict[str, list[tuple[float, float]]]]:
    grouped: dict[str, dict[str, list[tuple[float, float]]]] = defaultdict(lambda: defaultdict(list))
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["figure_group"] != "engine_n_emissions":
                continue
            grouped[row["panel_id"]][row["series_id"]].append((float(row["x_value"]), float(row["y_value"])))

    for panel_data in grouped.values():
        for points in panel_data.values():
            points.sort(key=lambda item: item[0])
    return grouped


def plot_panel(ax: plt.Axes, panel_id: str, series_data: dict[str, list[tuple[float, float]]]) -> None:
    for series_id, points in series_data.items():
        color, marker, label = STYLE[series_id]
        xs = [x for x, _ in points]
        ys = [y for _, y in points]
        ax.plot(xs, ys, color=color, marker=marker, linewidth=1.5, markersize=4, label=label)

    ax.set_xlim(0.8, 1.8)
    ax.set_ylim(*PANEL_CONFIG[panel_id]["ylim"])
    ax.set_xlabel(r"$\lambda$ [-]", fontsize=11)
    ax.set_ylabel(PANEL_CONFIG[panel_id]["ylabel"], fontsize=11)
    ax.tick_params(labelsize=8)
    ax.legend(frameon=False, fontsize=7, loc="upper left")


def main() -> None:
    configure_matplotlib()
    grouped = load_series()

    fig, axes = plt.subplots(1, 2, figsize=(8, 4.2), dpi=180)
    for ax, panel_id in zip(axes, ["left", "right"]):
        plot_panel(ax, panel_id, grouped[panel_id])

    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")


if __name__ == "__main__":
    main()

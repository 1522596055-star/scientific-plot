from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
DATA_PATH = ROOT / "data" / "shared" / "scatter_points_v1.csv"
OUTPUT_PATH = Path(__file__).resolve().parent / "output.png"
FIGURE_GROUP = "cluster_embedding"
COLORS = {
    "Cluster 1": "#1f78b4",
    "Cluster 2": "#e31a1c",
    "Cluster 3": "#33a02c",
    "Cluster 4": "#ff7f00",
}


def configure_matplotlib() -> None:
    plt.rcParams.update({"font.family": "DejaVu Sans"})


def load_points() -> dict[str, list[tuple[float, float, float]]]:
    grouped: dict[str, list[tuple[float, float, float]]] = defaultdict(list)
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["figure_group"] != FIGURE_GROUP:
                continue
            grouped[row["series_id"]].append((float(row["x"]), float(row["y"]), float(row["size"])))
    return grouped


def plot_cluster(ax: plt.Axes, label: str, points: list[tuple[float, float, float]]) -> None:
    xs = [x for x, _, _ in points]
    ys = [y for _, y, _ in points]
    sizes = [size for _, _, size in points]
    ax.scatter(xs, ys, s=sizes, alpha=0.65, color=COLORS[label], label=label)


def main() -> None:
    configure_matplotlib()
    grouped = load_points()

    fig, ax = plt.subplots(figsize=(5.4, 4.6), dpi=180)
    for label in sorted(grouped):
        plot_cluster(ax, label, grouped[label])

    ax.set_xlabel("Embedding dimension 1", fontsize=11)
    ax.set_ylabel("Embedding dimension 2", fontsize=11)
    ax.legend(frameon=False, fontsize=8)
    ax.tick_params(labelsize=8)

    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")


if __name__ == "__main__":
    main()

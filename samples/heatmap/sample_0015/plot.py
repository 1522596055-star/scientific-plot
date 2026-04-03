from __future__ import annotations

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
DATA_PATH = ROOT / "data" / "shared" / "matrix_values_v1.csv"
OUTPUT_PATH = Path(__file__).resolve().parent / "output.png"
FIGURE_GROUP = "method_correlation_heatmap"


def configure_matplotlib() -> None:
    plt.rcParams.update({"font.family": "DejaVu Sans"})


def load_matrix() -> tuple[list[str], list[str], np.ndarray]:
    row_labels: list[str] = []
    col_labels: list[str] = []
    values: dict[tuple[str, str], float] = {}

    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["figure_group"] != FIGURE_GROUP:
                continue
            row_id = row["row_id"]
            col_id = row["col_id"]
            row_labels.append(row_id)
            col_labels.append(col_id)
            values[(row_id, col_id)] = float(row["value"])

    ordered_rows = list(dict.fromkeys(row_labels))
    ordered_cols = list(dict.fromkeys(col_labels))
    matrix = np.array([[values[(row_id, col_id)] for col_id in ordered_cols] for row_id in ordered_rows])
    return ordered_rows, ordered_cols, matrix


def annotation_color(value: float) -> str:
    return "white" if value < 0.45 else "black"


def annotate_cells(ax: plt.Axes, matrix: np.ndarray) -> None:
    for row_index in range(matrix.shape[0]):
        for col_index in range(matrix.shape[1]):
            value = matrix[row_index, col_index]
            ax.text(
                col_index,
                row_index,
                f"{value:.2f}",
                ha="center",
                va="center",
                fontsize=6,
                color=annotation_color(value),
            )


def main() -> None:
    configure_matplotlib()
    row_labels, col_labels, matrix = load_matrix()

    fig, ax = plt.subplots(figsize=(6.2, 5.2), dpi=180)
    image = ax.imshow(matrix, cmap="viridis", vmin=0, vmax=1)

    ax.set_xticks(range(len(col_labels)))
    ax.set_xticklabels(col_labels, rotation=45, ha="right", fontsize=8)
    ax.set_yticks(range(len(row_labels)))
    ax.set_yticklabels(row_labels, fontsize=8)
    annotate_cells(ax, matrix)

    fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)
    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")


if __name__ == "__main__":
    main()

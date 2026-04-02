from __future__ import annotations
import csv
from collections import defaultdict
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
DATA_PATH = ROOT / 'data' / 'shared' / 'categorical_measurements_v1.csv'
OUTPUT_PATH = Path(__file__).resolve().parent / 'output.png'
PANELS = ['a', 'b']
TITLES = {'a': 'T = 1100 K', 'b': 'T = 1400 K'}

def load():
    grouped = defaultdict(list)
    with DATA_PATH.open(newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if row['figure_group'] != 'idt_sensitivity':
                continue
            grouped[row['condition_id']].append((row['category_id'], float(row['mean_value'])))
    return grouped

def main():
    plt.rcParams.update({'font.family':'DejaVu Sans','axes.linewidth':1.0})
    grouped = load()
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 4.2), dpi=180, sharex=True)
    for ax, panel in zip(axes, PANELS):
        items = grouped[panel]
        labels = [i[0] for i in items]
        vals = [i[1] for i in items]
        y = list(range(len(labels)))
        colors = ['#c51616' if v > 0 else '#1b2fd8' for v in vals]
        ax.barh(y, vals, color=colors)
        ax.axvline(0, color='black', linewidth=0.8)
        ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=7)
        ax.invert_yaxis(); ax.set_xlim(-0.6, 0.6)
        ax.set_title(TITLES[panel], fontsize=10, fontweight='bold', color='#117722')
        ax.tick_params(axis='x', labelsize=8)
    axes[0].set_xlabel('Sensitivity coefficient', fontsize=10)
    axes[1].set_xlabel('Sensitivity coefficient', fontsize=10)
    fig.tight_layout(); fig.savefig(OUTPUT_PATH, bbox_inches='tight')

if __name__ == '__main__': main()

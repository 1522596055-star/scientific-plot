from __future__ import annotations
import csv
from collections import defaultdict
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
DATA_PATH = ROOT / 'data' / 'shared' / 'profile_series_v1.csv'
OUTPUT_PATH = Path(__file__).resolve().parent / 'output.png'
PANELS = ['left', 'right']
PANEL_CFG = {'left': {'title': 'HAB = 25 mm'}, 'right': {'title': 'HAB = 50 mm'}}
STYLE = {
    'meas_base': {'kind': 'point', 'color': '#56a45b', 'marker': 'o', 'label': 'Meas, Base'},
    'meas_doped': {'kind': 'point', 'color': '#f09a62', 'marker': '^', 'label': 'Meas, Doped'},
    'model_base': {'kind': 'line', 'color': '#56a45b', 'ls': '--', 'label': '1D-CF, Base'},
    'model_doped': {'kind': 'line', 'color': '#f09a62', 'ls': '-', 'label': '1D-CF, Doped'},
}

def load():
    grouped = defaultdict(lambda: defaultdict(list))
    with DATA_PATH.open(newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if row['figure_group'] != 'ells_profile_comparison':
                continue
            grouped[row['panel_id']][row['series_id']].append((float(row['x_value']), float(row['y_value']), float(row['error_high'])))
    for p in grouped:
        for s in grouped[p]: grouped[p][s].sort()
    return grouped

def main():
    plt.rcParams.update({'font.family':'DejaVu Serif','axes.linewidth':1.1})
    grouped = load()
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4), dpi=180)
    for ax, panel in zip(axes, PANELS):
        for sid, style in STYLE.items():
            pts = grouped[panel][sid]
            xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
            if style['kind'] == 'line':
                ax.plot(xs, ys, color=style['color'], linestyle=style['ls'], linewidth=1.8, label=style['label'])
            else:
                yerr = [p[2] for p in pts]
                ax.errorbar(xs, ys, yerr=yerr, fmt=style['marker'], color=style['color'], markersize=4.5, linestyle='None', label=style['label'])
        ax.set_xlim(-10, 14); ax.set_ylim(0.05, 0.10)
        ax.set_xlabel('x, mm', fontsize=12); ax.set_ylabel(r'$Q_{0,0} / Q_{0,0,ref}$', fontsize=12)
        ax.text(0.08, 0.12, PANEL_CFG[panel]['title'], transform=ax.transAxes, fontsize=11, fontweight='bold')
        ax.tick_params(labelsize=9)
    axes[0].legend(frameon=False, fontsize=9, loc='upper center', ncol=2)
    fig.tight_layout(); fig.savefig(OUTPUT_PATH, bbox_inches='tight')

if __name__ == '__main__':
    main()

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
STYLE = {
    'nh3_lpilot': ('#111111', '^', 'L-pilot NH3'), 'nh3_epilot': ('#e33', 'o', 'E-pilot NH3'),
    'nox_lpilot': ('#111111', '^', 'L-pilot NOx'), 'nox_epilot': ('#e33', 'o', 'E-pilot NOx'),
    'cdc_nox': ('#4477ff', None, 'CDC (NOx)'), 'n2o_lpilot': ('#111111', '^', 'L-pilot N2O'),
    'n2o_epilot': ('#e33', 'o', 'E-pilot N2O'), 'cdc_n2o': ('#4477ff', None, 'CDC (N2O)')
}

def load():
    grouped = defaultdict(lambda: defaultdict(list))
    with DATA_PATH.open(newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if row['figure_group'] != 'engine_n_emissions': continue
            grouped[row['panel_id']][row['series_id']].append((float(row['x_value']), float(row['y_value'])))
    return grouped

def main():
    grouped = load(); plt.rcParams.update({'font.family':'DejaVu Serif'})
    fig, axes = plt.subplots(1, 2, figsize=(8, 4.2), dpi=180)
    for ax, panel in zip(axes, ['left', 'right']):
        for sid, pts in grouped[panel].items():
            color, marker, label = STYLE[sid]
            xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
            ax.plot(xs, ys, color=color, marker=marker, linewidth=1.5, markersize=4, label=label)
        ax.set_xlim(0.8, 1.8); ax.set_xlabel(r'$\lambda$ [-]', fontsize=11); ax.tick_params(labelsize=8)
    axes[0].set_ylim(0, 12000); axes[1].set_ylim(0, 60)
    axes[0].set_ylabel('NH3 / NOx [ppm]', fontsize=11); axes[1].set_ylabel('N2O [ppm]', fontsize=11)
    axes[0].legend(frameon=False, fontsize=7, loc='upper left'); axes[1].legend(frameon=False, fontsize=7, loc='upper left')
    fig.tight_layout(); fig.savefig(OUTPUT_PATH, bbox_inches='tight')

if __name__ == '__main__': main()

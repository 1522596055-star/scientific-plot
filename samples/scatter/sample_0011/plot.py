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
STYLE = {'nc10': ('#d95f02', 'o'), 'ic8': ('#1f78b4', '^'), 'nh3_blend': ('#4daf4a', 's'), 'nc10_twe': ('#d95f02', 'o'), 'ic8_twe': ('#1f78b4', '^'), 'nh3_twe': ('#4daf4a', 's')}

def load():
    grouped = defaultdict(lambda: defaultdict(list))
    with DATA_PATH.open(newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if row['figure_group'] != 'extinction_limits': continue
            grouped[row['panel_id']][row['series_id']].append((float(row['x_value']), float(row['y_value'])))
    return grouped

def main():
    grouped = load(); plt.rcParams.update({'font.family':'DejaVu Serif'})
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.6), dpi=180)
    for sid, pts in grouped['left'].items():
        c,m=STYLE[sid]; axes[0].scatter([p[0] for p in pts],[p[1] for p in pts], color=c, marker=m, s=20, label=sid.replace('_',' '))
    for sid, pts in grouped['right'].items():
        c,m=STYLE[sid]; axes[1].scatter([p[0] for p in pts],[p[1] for p in pts], color=c, marker=m, s=20, label=sid.replace('_twe',''))
    axes[0].set_xlim(0,1.0); axes[0].set_ylim(0,300); axes[0].set_xlabel('Fuel mole fraction'); axes[0].set_ylabel(r'$a_E$ [1/s]')
    axes[1].set_xlim(0,3.0); axes[1].set_ylim(0,3.5); axes[1].set_xlabel('TWE [cal/cm$^3$]'); axes[1].set_ylabel(r'$a_E$ [1/s] x 10$^{-2}$')
    axes[0].legend(frameon=False, fontsize=7, loc='upper left')
    fig.tight_layout(); fig.savefig(OUTPUT_PATH, bbox_inches='tight')

if __name__ == '__main__': main()

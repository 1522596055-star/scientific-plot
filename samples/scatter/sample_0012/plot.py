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
STYLE = {'hefa': ('#444444', 'o'), 'hefa_pmt': ('#1f78b4', 's'), 'hefa_dmco': ('#33a02c', 'D'), 'hefa_nbch': ('#e31a1c', '^')}
LABEL = {'hefa':'HEFA','hefa_pmt':'HEFA + PMT','hefa_dmco':'HEFA + DMCO','hefa_nbch':'HEFA + nBCH'}

def load():
    grouped = defaultdict(list)
    with DATA_PATH.open(newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if row['figure_group'] != 'ignition_delay_comparison': continue
            grouped[row['series_id']].append((float(row['x_value']), float(row['y_value'])))
    return grouped

def main():
    grouped = load(); plt.rcParams.update({'font.family':'DejaVu Serif'})
    fig, ax = plt.subplots(figsize=(4.8, 4.2), dpi=180)
    for sid, pts in grouped.items():
        xs=[p[0] for p in pts if p[1] > 0]; ys=[p[1] for p in pts if p[1] > 0]
        c,m=STYLE[sid]
        ax.plot(xs, ys, color=c, marker=m, markersize=4, linewidth=1.0, linestyle='None', label=LABEL[sid])
    ax.set_xlim(0.70,0.85); ax.set_yscale('log'); ax.set_ylim(60,1500)
    ax.set_xlabel(r'1000/T [K$^{-1}$]', fontsize=11); ax.set_ylabel('Ignition Delay Time [us]', fontsize=11)
    ax.legend(frameon=False, fontsize=7, loc='upper left')
    ax.tick_params(labelsize=8)
    fig.tight_layout(); fig.savefig(OUTPUT_PATH, bbox_inches='tight')

if __name__ == '__main__': main()

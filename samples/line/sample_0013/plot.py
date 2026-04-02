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
STYLE={'5C':('#111111','-'),'10C':('#ff4d4d','--'),'20C':('#2ca02c','-.'),'30C':('#cc66cc',':')}
LABEL={'5C':'5°C/min','10C':'10°C/min','20C':'20°C/min','30C':'30°C/min'}

def load():
    grouped=defaultdict(list)
    with DATA_PATH.open(newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if row['figure_group']!='polymer_mass_loss': continue
            grouped[row['series_id']].append((float(row['x_value']), float(row['y_value'])))
    return grouped

def main():
    grouped=load(); plt.rcParams.update({'font.family':'DejaVu Serif'})
    fig,ax=plt.subplots(figsize=(4.6,4.0), dpi=180)
    for sid,pts in grouped.items():
        c,ls=STYLE[sid]
        ax.plot([p[0] for p in pts],[p[1] for p in pts], color=c, linestyle=ls, linewidth=1.5, label=LABEL[sid])
    ax.set_xlim(200,500); ax.set_ylim(0,105)
    ax.set_xlabel('Temperature (°C)', fontsize=11); ax.set_ylabel('Weight %', fontsize=11)
    ax.legend(frameon=False, fontsize=8, loc='upper right'); ax.tick_params(labelsize=8)
    fig.tight_layout(); fig.savefig(OUTPUT_PATH, bbox_inches='tight')

if __name__=='__main__': main()

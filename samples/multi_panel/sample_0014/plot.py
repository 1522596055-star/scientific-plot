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
STYLE={'md_ce':('#30d44f','o','Methanol/Diesel RCCI'),'ad_ce':('#3255ff','o','Ammonia/Diesel RCCI'),'md_ite':('#30d44f','o','Methanol/Diesel RCCI'),'ad_ite':('#3255ff','o','Ammonia/Diesel RCCI')}

def load():
    grouped=defaultdict(lambda: defaultdict(list))
    with DATA_PATH.open(newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if row['figure_group']!='rcci_efficiency': continue
            grouped[row['panel_id']][row['series_id']].append((float(row['x_value']), float(row['y_value'])))
    return grouped

def main():
    grouped=load(); plt.rcParams.update({'font.family':'DejaVu Serif'})
    fig,axes=plt.subplots(2,1, figsize=(4.5,8.2), dpi=180)
    for ax,panel,ylab,ylim in [(axes[0],'top','Combustion Efficiency [%]',(60,100)),(axes[1],'bottom','Gross ITE [%]',(30,55))]:
        for sid,pts in grouped[panel].items():
            c,m,l=STYLE[sid]
            ax.plot([p[0] for p in pts],[p[1] for p in pts], color=c, marker=m, markersize=3.5, linewidth=1.2, markerfacecolor='white', label=l)
        ax.set_xlim(0,0.8); ax.set_ylim(*ylim); ax.set_xlabel('Premixed Energy Ratio', fontsize=11); ax.set_ylabel(ylab, fontsize=11); ax.tick_params(labelsize=8)
    axes[0].legend(frameon=False, fontsize=7, loc='lower left'); axes[1].legend(frameon=False, fontsize=7, loc='lower left')
    fig.tight_layout(); fig.savefig(OUTPUT_PATH, bbox_inches='tight')

if __name__=='__main__': main()

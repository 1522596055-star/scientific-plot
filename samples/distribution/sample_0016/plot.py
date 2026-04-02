from __future__ import annotations
import csv
from collections import defaultdict
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
DATA_PATH = ROOT / 'data' / 'shared' / 'distribution_measurements_v1.csv'
OUTPUT_PATH = Path(__file__).resolve().parent / 'output.png'
ORDER=['Baseline','Regularized','Ensemble','Ours']

def load():
    grouped=defaultdict(list)
    with DATA_PATH.open(newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if row['figure_group']!='model_score_distribution': continue
            grouped[row['series_id']].append(float(row['value']))
    return grouped

def main():
    grouped=load(); plt.rcParams.update({'font.family':'DejaVu Sans'})
    fig,ax=plt.subplots(figsize=(5.6,4.2), dpi=180)
    data=[grouped[k] for k in ORDER]
    bp=ax.boxplot(data, patch_artist=True, tick_labels=ORDER, showfliers=True)
    colors=['#bdbdbd','#80b1d3','#8dd3c7','#fb8072']
    for patch,c in zip(bp['boxes'],colors): patch.set_facecolor(c)
    ax.set_ylabel('Validation score', fontsize=11); ax.tick_params(labelsize=8)
    fig.tight_layout(); fig.savefig(OUTPUT_PATH, bbox_inches='tight')
if __name__=='__main__': main()

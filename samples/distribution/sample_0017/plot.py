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
ORDER=['Control','Treatment A','Treatment B','Treatment C']

def load():
    grouped=defaultdict(list)
    with DATA_PATH.open(newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if row['figure_group']!='cell_response_distribution': continue
            grouped[row['series_id']].append(float(row['value']))
    return grouped

def main():
    grouped=load(); plt.rcParams.update({'font.family':'DejaVu Sans'})
    fig,ax=plt.subplots(figsize=(5.8,4.2), dpi=180)
    parts=ax.violinplot([grouped[k] for k in ORDER], showmeans=False, showmedians=True)
    colors=['#b3cde3','#ccebc5','#fbb4ae','#decbe4']
    for body,c in zip(parts['bodies'],colors): body.set_facecolor(c); body.set_alpha(0.85)
    ax.set_xticks(range(1,len(ORDER)+1)); ax.set_xticklabels(ORDER, fontsize=8)
    ax.set_ylabel('Response level', fontsize=11)
    fig.tight_layout(); fig.savefig(OUTPUT_PATH, bbox_inches='tight')
if __name__=='__main__': main()

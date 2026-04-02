from __future__ import annotations
import csv
from collections import defaultdict
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
DATA_PATH = ROOT / 'data' / 'shared' / 'scatter_points_v1.csv'
OUTPUT_PATH = Path(__file__).resolve().parent / 'output.png'
COLORS={'Cluster 1':'#1f78b4','Cluster 2':'#e31a1c','Cluster 3':'#33a02c','Cluster 4':'#ff7f00'}

def load():
    grouped=defaultdict(list)
    with DATA_PATH.open(newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if row['figure_group']!='cluster_embedding': continue
            grouped[row['series_id']].append((float(row['x']), float(row['y']), float(row['size'])))
    return grouped

def main():
    grouped=load(); plt.rcParams.update({'font.family':'DejaVu Sans'})
    fig,ax=plt.subplots(figsize=(5.4,4.6), dpi=180)
    for sid,pts in grouped.items():
        ax.scatter([p[0] for p in pts],[p[1] for p in pts], s=[p[2] for p in pts], alpha=0.65, color=COLORS[sid], label=sid)
    ax.set_xlabel('Embedding dimension 1', fontsize=11); ax.set_ylabel('Embedding dimension 2', fontsize=11)
    ax.legend(frameon=False, fontsize=8); ax.tick_params(labelsize=8)
    fig.tight_layout(); fig.savefig(OUTPUT_PATH, bbox_inches='tight')
if __name__=='__main__': main()

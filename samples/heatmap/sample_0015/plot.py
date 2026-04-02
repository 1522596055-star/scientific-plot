from __future__ import annotations
import csv
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
DATA_PATH = ROOT / 'data' / 'shared' / 'matrix_values_v1.csv'
OUTPUT_PATH = Path(__file__).resolve().parent / 'output.png'

def load_matrix():
    rows=[]; cols=[]; vals={}
    with DATA_PATH.open(newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if row['figure_group']!='method_correlation_heatmap': continue
            rows.append(row['row_id']); cols.append(row['col_id']); vals[(row['row_id'],row['col_id'])]=float(row['value'])
    row_ids=list(dict.fromkeys(rows)); col_ids=list(dict.fromkeys(cols))
    mat=np.array([[vals[(r,c)] for c in col_ids] for r in row_ids])
    return row_ids,col_ids,mat

def main():
    row_ids,col_ids,mat=load_matrix(); plt.rcParams.update({'font.family':'DejaVu Sans'})
    fig,ax=plt.subplots(figsize=(6.2,5.2), dpi=180)
    im=ax.imshow(mat, cmap='viridis', vmin=0, vmax=1)
    ax.set_xticks(range(len(col_ids))); ax.set_xticklabels(col_ids, rotation=45, ha='right', fontsize=8)
    ax.set_yticks(range(len(row_ids))); ax.set_yticklabels(row_ids, fontsize=8)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            ax.text(j, i, f'{mat[i,j]:.2f}', ha='center', va='center', fontsize=6, color='white' if mat[i,j] < 0.45 else 'black')
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    fig.tight_layout(); fig.savefig(OUTPUT_PATH, bbox_inches='tight')
if __name__=='__main__': main()

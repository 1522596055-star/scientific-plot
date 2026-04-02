from __future__ import annotations
import csv
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
DATA_PATH = ROOT / 'data' / 'shared' / 'distribution_measurements_v1.csv'
OUTPUT_PATH = Path(__file__).resolve().parent / 'output.png'

def load():
    values=[]
    with DATA_PATH.open(newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if row['figure_group']=='particle_size_histogram': values.append(float(row['value']))
    return values

def main():
    values=load(); plt.rcParams.update({'font.family':'DejaVu Sans'})
    fig,ax=plt.subplots(figsize=(5.4,4.0), dpi=180)
    ax.hist(values, bins=18, color='#80b1d3', edgecolor='white')
    ax.set_xlabel('Particle size [nm]', fontsize=11); ax.set_ylabel('Count', fontsize=11); ax.tick_params(labelsize=8)
    fig.tight_layout(); fig.savefig(OUTPUT_PATH, bbox_inches='tight')
if __name__=='__main__': main()

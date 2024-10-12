# py -m src.scripts.per_laboratory
# py .\src\scripts\per_laboratory.py

import pandas as pd
import matplotlib.pyplot as plt
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2] / 'src'))
from utils.util import random_hex_color

df = pd.read_csv('data/data.csv')

laboratorio_count = df['LABORATÓRIO'].value_counts()

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(laboratorio_count.index, laboratorio_count.values, color=random_hex_color(), edgecolor='black', linewidth=1)

ax.set_title('Distribuição dos Candidatos por Laboratório', fontsize=16)
ax.set_xlabel('Laboratório', fontsize=12)
ax.set_ylabel('Quantidade de Candidatos', fontsize=12)
ax.set_xticklabels(laboratorio_count.index, rotation=45)
ax.grid(axis='y')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 1, int(yval), ha='center', va='bottom', fontsize=10)

fig.tight_layout()
fig.savefig('outputs/distribuicao_por_laboratorio.png', format='png', dpi=300, bbox_inches='tight')

plt.show()

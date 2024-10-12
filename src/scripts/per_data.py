import pandas as pd
import matplotlib.pyplot as plt
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2] / 'src'))
from utils.util import random_hex_color

df = pd.read_csv(Path(__file__).resolve().parents[2] / 'data/data.csv')

data_count = df['DATA'].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(data_count.index, data_count.values, color=random_hex_color(), edgecolor='black', linewidth=1)

ax.set_title('Distribuição dos Candidatos por Data', fontsize=16)
ax.set_xlabel('Data', fontsize=12)
ax.set_ylabel('Quantidade de Candidatos', fontsize=12)
ax.set_xticks(range(len(data_count)))
ax.set_xticklabels(data_count.index, rotation=0)
ax.grid(axis='y')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 1, int(yval), ha='center', va='bottom', fontsize=10)

fig.tight_layout()
output_path = Path(__file__).resolve().parents[2] / 'outputs/distribuicao_por_data.png'
fig.savefig(output_path, format='png', dpi=300, bbox_inches='tight')

plt.show()
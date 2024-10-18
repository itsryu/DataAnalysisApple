# py -m src.scripts.new_devs.py
# py .\src\scripts\new_devs.py

import pandas as pd
import matplotlib.pyplot as plt
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2] / 'src'))
from utils.util import random_hex_color

df = pd.read_csv('data/data.csv')

# verificando se o candidato é calouro ou veterano com base na matrícula iniciada com UC e ano de ingresso
df['CALOURO'] = df['MATRICULA'].apply(lambda x: 'VETERANO' if x.startswith('UC') and int(x[2:4]) <= 23 else 'CALOURO')
df['CATEGORIA'] = df['CATEGORIA'].str.upper().apply(lambda x: 'DESIGNER' if 'DESIGNER' in x else 'DESENVOLVEDOR')

count = df.value_counts(['CALOURO', 'CATEGORIA']).reset_index(name='QUANTIDADE')

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(count['CALOURO'] + ' - ' + count['CATEGORIA'], count['QUANTIDADE'], color=random_hex_color(), edgecolor='black', linewidth=1)

ax.set_title('Calouros vs Veteranos Candidatos por Categoria', fontsize=16)
ax.set_ylabel('Quantidade de Candidatos', fontsize=12)
ax.grid(axis='y')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 1, int(yval), ha='center', va='bottom')

output_path = Path(__file__).resolve().parents[2] / 'outputs/calouros_vs_veteranos_por_categoria.png'
fig.savefig(output_path, format='png', dpi=300, bbox_inches='tight')

plt.show()
# py -m src.scripts.vacancies_by_category
# py .\src\scripts\vacancies_by_category.py

import pandas as pd
import matplotlib.pyplot as plt
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2] / 'src'))
from utils.util import random_hex_color

df = pd.read_csv('data/data.csv')

count = df['CATEGORIA'].value_counts().reset_index()
count.columns = ['CATEGORIA', 'QUANTIDADE_CANDIDATOS']
vagas = {'DESIGNER': 30, 'DESENVOLVEDOR': 70}
count['VAGAS'] = count['CATEGORIA'].map(vagas)
count['TAXA_OCUPACAO'] = (count['QUANTIDADE_CANDIDATOS'] / count['VAGAS']) * 100

# plotting
fig, ax = plt.subplots(figsize=(10, 6))
category_color = random_hex_color()
vacancies_color = random_hex_color()
edge_color = 'black'

barA = ax.bar(count['CATEGORIA'], count['QUANTIDADE_CANDIDATOS'], color=category_color, edgecolor=edge_color, label='Candidatos')
barB = ax.bar(count['CATEGORIA'], count['VAGAS'], color=vacancies_color, edgecolor=edge_color, label='Vagas')

for bar in barA + barB:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 1, int(yval), ha='center', va='bottom')

# add vertical lines and proportion text
for i, row in count.iterrows():
    x = i
    y_vagas = row['VAGAS']
    y_candidatos = row['QUANTIDADE_CANDIDATOS']
    ax.vlines(x + 0.1, y_vagas, y_candidatos, color='red', linestyle='--', lw=2)
    if y_vagas > 0:
        proporcao = y_candidatos / y_vagas
        ax.text(x + 0.15, (y_vagas + y_candidatos) / 2, f'{proporcao:.2f}', color='red', ha='center', va='center')

ax.set_title('Candidatos vs Vagas por Categoria', fontsize=16)
ax.set_ylabel('Quantidade', fontsize=12)
ax.grid(axis='y')
ax.legend()

plt.tight_layout()
plt.savefig('outputs/vagas_por_categoria.png', format='png', dpi=300, bbox_inches='tight')
plt.show()

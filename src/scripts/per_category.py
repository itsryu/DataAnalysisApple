# py -m src.scripts.per_category
# py .\src\scripts\per_category.py

import pandas as pd
import matplotlib.pyplot as plt
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2] / 'src'))
from utils.util import random_hex_color, func

# Load data
df = pd.read_csv('data/data.csv')

# Count occurrences of each category
count = df['CATEGORIA'].value_counts()

# Calculate totals
total = len(df)
total_developers = count.get('DESENVOLVEDOR', 0)
total_designers = count.get('DESIGNER', 0)

# Plotting
labels = ['Total de Desenvolvedores', 'Total de Designers']
sizes = [total_developers, total_designers]
colors = [random_hex_color(), random_hex_color()]

fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# Pie chart
axs[0].pie(sizes, labels=labels, colors=colors, autopct=lambda pct: func(pct, sizes), startangle=140)
axs[0].set_title('Candidatos por Categorias', fontsize=10)
axs[0].axis('equal')
axs[0].text(0, -1.2, f'Total de Inscritos: {total}', ha='center', fontsize=10)

# Bar chart
bar_colors = [colors[0] if category == 'DESENVOLVEDOR' else colors[1] if category == 'DESIGNER' else random_hex_color() for category in count.index]
count.plot(kind='bar', color=bar_colors, ax=axs[1], edgecolor='black')
axs[1].set_xlabel('Categoria', fontsize=10)
axs[1].set_ylabel('Quantidade', fontsize=10)
axs[1].set_xticklabels(count.index, rotation=0)
axs[1].grid(axis='y')

plt.tight_layout()
plt.savefig('outputs/candidatos_por_categoria.png', format='png', dpi=300, bbox_inches='tight')
plt.show()
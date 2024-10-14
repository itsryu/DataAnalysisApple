import pandas as pd
import matplotlib.pyplot as plt
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2] / 'src'))
from utils.util import random_hex_color, func

df = pd.read_csv('data/data.csv')

count = df['CATEGORIA'].value_counts()
total = len(df)

labels = ['Total de Desenvolvedores', 'Total de Designers']
sizes = [count.get('DESENVOLVEDOR', 01, count.get('DESIGNER', 0)]
colors = [random_hex_color(), random_hex_color()]

fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# pie
axs[0].pie(sizes, labels=labels, colors=colors, autopct=lambda pct: func(pct, sizes), startangle=140)
axs[0].set_title('Candidatos por Categorias', fontsize=10)
axs[0].axis('equal')
axs[0].text(0, -1.2, f'Total de Inscritos: {total}', ha='center', fontsize=10)

# bar
bar_colors = [colors[0] if category == 'DESENVOLVEDOR' else colors[1] if category == 'DESIGNER' else random_hex_color() for category in count.index]
bars = count.plot(kind='bar', color=bar_colors, ax=axs[1], edgecolor='black')
axs[1].set_xlabel('Categoria', fontsize=10)
axs[1].set_ylabel('Quantidade', fontsize=10)
axs[1].set_xticklabels(count.index, rotation=0)
axs[1].grid(axis='y')

for bar in bars.patches:
    axs[1].annotate(f'{int(bar.get_height())}', xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')

plt.tight_layout()
plt.savefig('outputs/candidatos_por_categoria.png', format='png', dpi=300, bbox_inches='tight')
plt.show()

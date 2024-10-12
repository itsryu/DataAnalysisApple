# py -m src.scripts.histogram
# py .\src\scripts\histogram.py

import pandas as pd
import matplotlib.pyplot as plt
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2] / 'src'))
from utils.util import random_hex_color

df = pd.read_csv('data/data.csv')

df['HORÁRIO_INICIO'] = pd.to_datetime(df['HORÁRIO'].str.split(' - ').str[0], format='%H:%M').dt.hour

plt.figure(figsize=(12, 6), dpi=80)
counts, bins, patches = plt.hist(df['HORÁRIO_INICIO'], bins=range(25), color=random_hex_color(), alpha=0.7, edgecolor='black', linewidth=1)

plt.title('Histograma de Horários dos Candidatos', fontsize=16)
plt.xlabel('Hora do Dia', fontsize=12)
plt.ylabel('Quantidade de Candidatos', fontsize=12)
plt.xticks(range(24))
plt.grid(axis='y')

for count, x in zip(counts, bins):
    if count > 0:
        plt.text(x + 0.5, count + 1, int(count), ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('outputs/histograma_horarios.png', format='png', dpi=300, bbox_inches='tight')
plt.show()

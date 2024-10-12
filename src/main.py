import pandas as pd
import pdfplumber
import matplotlib.pyplot as plt

path = "./PS_2024_INSCRITOS_LOCAL_DE_PROVA.pdf"

def extract_data_from_pdf(path):
    with pdfplumber.open(path) as pdf:
        data = []
        for page in pdf.pages:
            text = page.extract_text()
            lines = text.split('\n')
            for line in lines:
                row = line.split()
                data.append(row)
    return data

def fix_data(row):
    if len(row) > 7:
        row[5] = f"{row[5]} - {row[7]}"
        return row[:6]
    return row

data = extract_data_from_pdf(path)
data = [fix_data(row) for row in data]

# assuming the first row contains the headers
df = pd.DataFrame(data[1:], columns=data[0][:6])

# count occurrences of each category
count = df['CATEGORIA'].value_counts()

# calculate totals
total = df.shape[0]
total_developers = count.get('DESENVOLVEDOR', 0)
total_designers = count.get('DESIGNER', 0)

# plotting
labels = ['Total de Desenvolvedores', 'Total de Designers']
sizes = [total_developers, total_designers]
colors = ['#ff9999', '#66b3ff']

def func(pct, allvalues):
    absolute = int(pct / 100. * sum(allvalues))
    return f"{absolute} ({pct:.1f}%)"

fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# pie chart
axs[0].pie(sizes, labels=labels, colors=colors, autopct=lambda pct: func(pct, sizes), startangle=140)
axs[0].set_title('Distribuição por Categorias e Total', fontsize=10)
axs[0].axis('equal')
axs[0].text(0, -1.2, f'Total de Inscritos: {total}', ha='center', fontsize=10)

# bar chart
count.plot(kind='bar', color='skyblue', ax=axs[1], edgecolor='black')
axs[1].set_xlabel('Categoria', fontsize=10)
axs[1].set_ylabel('Quantidade', fontsize=10)
axs[1].set_xticklabels(count.index, rotation=0)
axs[1].grid(axis='y')

plt.tight_layout()
plt.show()
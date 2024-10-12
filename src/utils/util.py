import random
import pdfplumber

def random_hex_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def extract_data_from_pdf(path):
    with pdfplumber.open(path) as pdf:
        data = []
        for page in pdf.pages:
            text = page.extract_text()
            if text:
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

def func(pct, allvalues):
    absolute = int(pct / 100. * sum(allvalues))
    return f"{absolute} ({pct:.1f}%)"
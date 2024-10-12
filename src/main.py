import pandas as pd
from utils.util import extract_data_from_pdf, fix_data
from pathlib import Path

def main():
    path = Path("./PS_2024_INSCRITOS_LOCAL_DE_PROVA.pdf")
    
    try:
        data = extract_data_from_pdf(path)
        data = [fix_data(row) for row in data]
        
        # Exporting data to csv file
        df = pd.DataFrame(data[1:], columns=data[0][:6])
        output_path = Path('data/data.csv')
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False)
        
        print(f"Data successfully exported to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
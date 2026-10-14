import os
import glob
import pandas as pd
from sqlalchemy import create_engine

# 1. DB Name 'practice.db' set karein
db_path = "practice.db"
engine = create_engine(f"sqlite:///{db_path}")

# 2. 'raw_data' folder se CSV files read karein
raw_data_folder = "raw_data"
csv_files = glob.glob(os.path.join(raw_data_folder, "*.csv"))

print(f"Total {len(csv_files)} CSV files mili hain. 'practice.db' me save ho raha hai...\n")

# 3. Loop chala kar sabhi CSVs ko 'practice.db' me Tables banayein
for file_path in csv_files:
    filename = os.path.basename(file_path)
    
    # Table ka naam clean karein (e.g., 'olist_customers_dataset.csv' -> 'customers')
    table_name = filename.replace('.csv', '').replace('olist_', '').replace('_dataset', '')

    print(f"Loading '{filename}' -> Table: '{table_name}'...")

    df = pd.read_csv(file_path)
    df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

print("\n Sabi CSV files successfully 'practice.db' me convert ho gayi hain!")
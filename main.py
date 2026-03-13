from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

file_path = "data/DATASET Technical Test Data Engineer.xlsx"

print("Starting ETL pipeline...")

df = extract_data(file_path)
print("Extract selesai")

df_clean = transform_data(df)
print("Transform selesai")

load_data(df_clean)

print("ETL pipeline selesai")
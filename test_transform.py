from src.extract import extract_data
from src.transform import transform_data

file_path = "data/DATASET Technical Test Data Engineer.xlsx"

# Extract
df = extract_data(file_path)

# Transform
df_clean = transform_data(df)

print("DATA SETELAH TRANSFORM:")
print(df_clean.head())

print("\nTOTAL ROW:", len(df_clean))
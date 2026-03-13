import pandas as pd

df = pd.read_excel("data/DATASET Technical Test Data Engineer.xlsx")

print("= PREVIEW DATA =")
print(df.head())

print("\n= DATA INFO =")
print(df.info())

print("\n= MISSING VALUES =")
print(df.isnull().sum())

print("\n= DUPLICATE ROWS =")
print(df.duplicated().sum())
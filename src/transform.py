import pandas as pd

def transform_data(df):

    df["sales_period"] = pd.to_datetime(
        df["sales_period (DD/MM/YYYY)"],
        errors="coerce"
    )

    df["outlet_code"] = df["outlet_code"].astype(str).str.strip()
    df["product_code"] = df["product_code"].astype(str).str.replace(".0","",regex=False)

    df = df.dropna()

    # remove corrupted outlet codes
    df = df[df["outlet_code"].str.len() < 15]

    df = df.drop_duplicates()

    return df
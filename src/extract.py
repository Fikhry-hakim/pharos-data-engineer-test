import pandas as pd


def extract_data(file_path):
    """
    Extract data from Excel file and ensure correct datatypes.
    """

    df = pd.read_excel(
        file_path,
        dtype={
            "outlet_code": str,
            "product_code": str
        }
    )

    return df
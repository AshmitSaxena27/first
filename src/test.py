"""
data_loader.py
Loads raw sales data from a CSV file into a pandas DataFrame.
"""

import pandas as pd


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    df = pd.read_csv(file_path)
    print(f"Loaded {len(df)} rows from {file_path}")
    print("dfghjk")
    return df


if __name__ == "__main__":
    data = load_csv("data/sales_raw.csv")
    print(data.head())
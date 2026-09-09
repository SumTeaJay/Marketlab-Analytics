import pandas as pd
import numpy as np

def audit_markets(df: pd.DataFrame) -> dict[str, object]:
    output_dict = {"Число строк": 0, "Отсутствующие обязательные столбцы": [], "Число пропусков по столбцам": 0, "Число повторяющихся строк": 0, "Число повторяющихся индексов": 0, "Число отрицательных цен": 0, "Число строк, где нарушена формула цены": 0}
    output_dict["Число строк"] = len(df.index)

    required_columns = {"demand_intercept", "demand_slope", "quantity", "price"}
    missing_columns = required_columns - set(df.columns)
    output_dict["Отсутствующие обязательные столбцы"] = missing_columns

    output_dict["Число пропусков по столбцам"] = df.isna().sum().to_dict()
    output_dict["Число повторяющихся строк"] = int(df.duplicated().sum())
    output_dict["Число повторяющихся индексов"] = len(df.index) - df.index.nunique()

    if not missing_columns:
        output_dict["Число отрицательных цен"] = (df["price"] < 0).sum()
        output_dict["Число строк, где нарушена формула цены"] = len(df[df["price"] != df["demand_intercept"] - df["demand_slope"] * df["quantity"]])

    return output_dict

def load_markets(path: str) -> pd.DataFrame:
    pass

def clean_markets(df: pd.DataFrame) -> pd.DataFrame:
    pass

def validate_markets(df: pd.DataFrame, expected_count=None) -> None:
    pass

def save_markets(df: pd.DataFrame, path: str) -> None:
    pass

def main():
    pass

if __name__ == "__main__":
    main()
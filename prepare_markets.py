import pandas as pd
import numpy as np

numeric_columns = ["demand_intercept", "demand_slope", "quantity", "price"]

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
    df = pd.read_csv(path, index_col="market_id")
    return df

def clean_markets(df: pd.DataFrame) -> pd.DataFrame:
    clean_df = df.copy()
    for column in numeric_columns:
        clean_df[column] = pd.to_numeric(clean_df[column], errors="coerce")

    clean_df = clean_df.dropna(subset=["demand_intercept", "demand_slope", "quantity", "price"])
    clean_df = clean_df.drop_duplicates()

    if clean_df.index.is_unique == False:
        raise ValueError("Существуют данные с одинаковыми идентификаторами!")

    clean_df["price"] = clean_df["demand_intercept"] - clean_df["demand_slope"] * clean_df["quantity"]
    clean_df = clean_df[clean_df["price"] > 0]

    clean_df = clean_df.sort_index()

    return clean_df

def validate_markets(df: pd.DataFrame, expected_count=None) -> None:
    required_columns = {
        "demand_intercept",
        "demand_slope",
        "quantity",
        "price",
    }

    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(f"Отсутствуют столбцы: {missing_columns}")

    if expected_count is not None and len(df) != expected_count:
        raise ValueError(f"Ожидалось {expected_count} строк, получено {len(df)}")

    if df.isna().any().any():
        raise ValueError("В таблице остались пропуски")

    if not df.index.is_unique:
        raise ValueError("Значения market_id повторяются")

    if (df["price"] < 0).any():
        raise ValueError("Обнаружены отрицательные цены")

    correct_prices = (df["demand_intercept"] - df["demand_slope"] * df["quantity"])

    if not (df["price"] == correct_prices).all():
        raise ValueError("Обнаружена ошибка в формуле цены")
    

def save_markets(df: pd.DataFrame, path: str) -> None:
    df.to_csv(path)

def main():
    df = load_markets(r"data\raw\markets.csv")
    df = clean_markets(df)
    validate_markets(df, expected_count=100)
    save_markets(df, r"data\processed\markets_clean.csv")

if __name__ == "__main__":
    main()
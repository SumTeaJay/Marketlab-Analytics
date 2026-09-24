import pandas as pd
import numpy as np
import csv

numeric_columns = ["demand_intercept", "demand_slope", "marginal_costs"]

def audit_markets(df: pd.DataFrame) -> dict[str, object]:
    output_dict = {"Число строк": 0, "Отсутствующие обязательные столбцы": [], "Число пропусков по столбцам": 0, "Число повторяющихся строк": 0, "Число повторяющихся индексов": 0}
    output_dict["Число строк"] = len(df.index)

    required_columns = {"demand_intercept", "demand_slope", "marginal_costs"}
    missing_columns = required_columns - set(df.columns)
    output_dict["Отсутствующие обязательные столбцы"] = missing_columns

    output_dict["Число пропусков по столбцам"] = df.isna().sum().to_dict()
    output_dict["Число повторяющихся строк"] = int(df.duplicated().sum())
    output_dict["Число повторяющихся индексов"] = len(df.index) - df.index.nunique()

    return output_dict

def load_markets(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, index_col="market_id")
    return df

def clean_markets(df: pd.DataFrame) -> pd.DataFrame:
    clean_df = df.copy()
    for column in numeric_columns:
        clean_df[column] = pd.to_numeric(clean_df[column], errors="coerce")

    clean_df = clean_df.dropna(subset=["demand_intercept", "demand_slope", "marginal_costs"])
    clean_df = clean_df.drop_duplicates()

    if clean_df.index.is_unique == False:
        raise ValueError("Существуют данные с одинаковыми идентификаторами!")

    clean_df = clean_df.sort_index()

    return clean_df

def validate_generated_markets(df: pd.DataFrame, expected_count=None) -> None:
    required_columns = {
        "demand_intercept",
        "demand_slope",
        "marginal_costs"
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
    

def save_data_frame(df: pd.DataFrame, path: str) -> None:
    df.to_csv(path)

def prepare_markets() -> None:
    df_prices = load_markets(r"data\raw\markets_prices_raw.csv")
    df_costs = load_markets(r"data\raw\markets_costs_raw.csv")

    markets = pd.merge(df_prices, df_costs, how="left", validate="one_to_one", on="market_id")
    audit_results = audit_markets(markets)

    with open(r"data\audit\markets_audit.csv", "w", encoding="utf-8", newline="") as audit_csv:
        writer = csv.DictWriter(audit_csv, fieldnames=[
                "Число строк", 
                "Отсутствующие обязательные столбцы", 
                "Число пропусков по столбцам", 
                "Число повторяющихся строк",
                "Число повторяющихся индексов"])
        writer.writeheader()
        writer.writerow(audit_results)        

    markets = clean_markets(markets)
    validate_generated_markets(markets, expected_count=100)
    save_data_frame(markets, r"data\processed\markets_clean.csv")
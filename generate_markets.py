import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from prepare_markets import audit_markets

def validate_markets(df, expected_count):
    if any(df["price"] < 0):
        raise ValueError("В таблице присутствует отрицательная цена!")

    if not df.index.is_unique:
        raise ValueError("В таблице присутствуют несколько одинаковых идентификаторов!")

    if len(df) != expected_count:
        raise ValueError("В таблице недостаточно строк!")

    return True

def generate_market_parameters(count=1, seed=42):
    rng = np.random.default_rng(seed)

    a = rng.integers(100, 1000, size=count)
    b = rng.integers(1, 10, size=count)
    Q = rng.integers(1, 10, size=count)

    return (a, b, Q)

def return_prices(a: np.array, b: np.array, Q: np.array) -> np.array:
    P = a - b * Q
    return P[P >= 0]

def create_data_frame(a: np.array, b: np.array, Q: np.array) -> pd.DataFrame:
    df = pd.DataFrame({
        "demand_intercept": a,
        "demand_slope": b,
        "quantity": Q,
    }, index = list(range(1, len(a) + 1)))
    df["price"] = return_prices(a, b, Q)
    df.index.name = "market_id"
    return df

def main():
    df = pd.read_csv(r"data\raw\markets.csv", index_col="market_id")
    print(audit_markets(df))

if __name__ == "__main__":
    main()
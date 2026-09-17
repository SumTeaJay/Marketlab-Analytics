import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generate_market_parameters(count=1, seed=42):
    rng = np.random.default_rng(seed)

    a = rng.integers(100, 1000, size=count)
    b = rng.integers(1, 10, size=count)
    cost = rng.integers(100, 1000, size=count)

    return (a, b, cost)

def create_data_frame_price(a: np.array, b: np.array) -> pd.DataFrame:
    df = pd.DataFrame({
        "demand_intercept": a,
        "demand_slope": b,
    }, index = list(range(1, len(a) + 1)))
    df.index.name = "market_id"
    return df

def create_data_frame_costs(cost: np.array) -> pd.DataFrame:
    df = pd.DataFrame({
        "marginal_costs": cost,
    }, index = list(range(1, len(cost) + 1)))
    df.index.name = "market_id"
    return df    

def generate_markets() -> None:
    price_parameters = generate_market_parameters(100)
    df_prices = create_data_frame_price(price_parameters[0], price_parameters[1])
    df_costs = create_data_frame_costs(price_parameters[2])

    df_prices.to_csv(r"data\raw\markets_prices_raw.csv")
    df_costs.to_csv(r"data\raw\markets_costs_raw.csv")
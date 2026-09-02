import numpy as np
import pandas as pd

def generate_market_parameters(count=1, seed=42):
    rng = np.random.default_rng(seed)

    a = rng.integers(1, 1000, size=count)
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
    parameters = generate_market_parameters(100)
    df = create_data_frame(parameters[0], parameters[1], parameters[2])
    df.to_csv(r"data\markets.csv")

    first_array = generate_market_parameters(10, 42)[0]
    second_array = generate_market_parameters(10, 42)[0]
    print(first_array == second_array)

if __name__ == "__main__":
    main()
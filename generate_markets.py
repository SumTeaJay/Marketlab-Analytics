import numpy as np
import pandas as pd

def generate_market_parameters(count=1, seed=42):
    rng = np.random.default_rng(seed)

    a = rng.integers(1, 1000, size=count)
    b = rng.integers(1, 1000, size=count)
    Q = rng.integers(1, 1000, size=count)

    return (a, b, Q)

def return_prices(a: np.array, b: np.array, Q: np.array) -> np.array:
    P = a - b * Q
    only_non_negative = P >= 0
    return P[only_non_negative]

def convert_to_data_frame(a: np.array, b: np.array, Q: np.array) -> pd.DataFrame:
    df = pd.DataFrame({
        "a": a,
        "b": b,
        "Q": Q,
    }, index = list(range(1, len(a) + 1)))
    df.index.name = "market_id"
    return df


def main():
    arrays = generate_market_parameters(100)
    print(convert_to_data_frame(arrays[0], arrays[1], arrays[2]))

if __name__ == "__main__":
    main()
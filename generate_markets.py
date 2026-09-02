import numpy as np

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
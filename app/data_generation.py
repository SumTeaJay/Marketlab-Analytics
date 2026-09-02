import numpy as np

def generate_market_parameters(count=1, seed=42):
    rng = np.random.default_rng(seed)

    a = rng.integers(1, 1000, size=count)
    b = rng.integers(1, 1000, size=count)
    Q = rng.integers(1, 1000, size=count)

    return (a, b, Q)
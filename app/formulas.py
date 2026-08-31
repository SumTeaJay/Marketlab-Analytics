import numpy as np

def return_prices(a: np.array, b: np.array, Q: np.array) -> np.array:
    P = a - b * Q
    only_non_negative = P >= 0
    return P[only_non_negative]
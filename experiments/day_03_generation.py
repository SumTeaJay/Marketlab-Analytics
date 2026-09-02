# 1. Сгенерировать десять целых чисел.
# 2. Сгенерировать десять вещественных чисел.
# 3. Повторить генерацию с одинаковым `seed`.
# 4. Проверить равенство двух результатов.
# 5. Сгенерировать допустимые `a`, `b` и `Q` для 100 рынков.

import numpy as np
from generate_markets import generate_market_parameters

rng = np.random.default_rng(67)

#1
integers_array = rng.integers(100, 1000, size=10)
print(integers_array)

#2
uniforms_array = rng.uniform(100, 1000, size=10)
print(uniforms_array)

#3-4
rng = np.random.default_rng(42)
first_array = rng.integers(1, 10)
second_array = rng.integers(1, 10)
print(first_array == second_array)

#5
print(generate_market_parameters(100, 42))



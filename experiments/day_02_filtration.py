#Упражение
# 1. Увеличить все цены на 10%.
# 2. Выбрать цены выше заданного значения.
# 3. Для массивов `a`, `b` и `Q` вычислить `P = a - b * Q`.
# 4. Оставить только строки с положительной ценой.
# 5. Сравнить один результат с ручным расчётом.

import numpy as np
from app.generation import return_prices

prices = np.arange(10, 1000, 50)

print(f"Исходные цены - {prices}")
print(f"Цены, увеличенные на 10% - {prices * 1.1}")

limit = prices > 500
print(f"Цены больше пятисот - {prices[limit]}")

a = np.arange(1000, 1100)
b = np.arange(1, 101)
Q = np.arange(200, 300)

print(return_prices(a, b, Q))

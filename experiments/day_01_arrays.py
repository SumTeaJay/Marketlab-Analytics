###Упражнение
# 1. Создать массив из пяти цен.
# 2. Получить первый и последний элементы.
# 3. Получить первые три элемента срезом.
# 4. Создать массив чисел от 1 до 100.
# 5. Вывести `shape` и `dtype` двух массивов.

import numpy as np

prices = np.array([100, 200, 3000, 5000, 40.12])
print(f"Первый элемент - {prices[0]}")
print(f"Последний элемент - {prices[-1]}")
print(f"Первые три элемента - {prices[0:3]}")

numbers = np.arange(1, 101)
print(f"Числа от 1 до 100 - {numbers}")

print(f"shape prices - {prices.shape}")
print(f"dtype prices - {prices.dtype}")

print(f"shape numbers - {numbers.shape}")
print(f"dtype numbers - {numbers.dtype}")
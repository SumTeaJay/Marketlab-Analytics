import pandas as pd
import numpy as np

#Упражнение
# 1. Создать таблицу из трёх рынков вручную.
# 2. Вывести первые строки.
# 3. Получить список столбцов.
# 4. Вывести один столбец.
# 5. Проверить типы данных.

#1
df = pd.DataFrame({
    "a": np.array([1, 2, 3]),
    "b": np.array([4, 5, 6]),
    "Q": np.array([7, 8, 9])
})

#2
print(df.head())

#3
print(df.columns)

#4
print(df["a"])

#5
print(df.dtypes)
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "country": ["Russia", "Russia", "USA", "China"],
    "currency": ["ruble", "ruble", "dollar", None],
    "landscape": [1_000_000, 1_000_000, 500_000, 800_000]
}, index=[1, 1, 2, 3])

df.index.name = "country_id"


print(f"Число пропусков - {df.isna().sum().sum()}")
print(f"Число дупликатов - {df.duplicated().sum().sum()}")
print(f"Уникальны ли индексы? Ответ: {df.index.is_unique}")
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "object_id": [
        "OBJ_001",
        "OBJ_002",
        "OBJ_003",
        "OBJ_004",
        "OBJ_005",
        "OBJ_006",
        "OBJ_007",
        "OBJ_008",
        "OBJ_009",
        "OBJ_009"
    ],
    "calculated_value": [
        125.40,
        98.75,
        210.10,
        75.30,
        340.80,
        56.90,
        180.00,
        420.50,
        132.25,
        250.00
    ],
    "control_value": [
        125.39,
        98.75,
        210.15,
        75.30,
        341.20,
        56.91,
        179.95,
        420.50,
        132.10,
        250.00
    ]
})

too_distant_values = df[~np.isclose(df["calculated_value"], df["control_value"])]
tolerance = 0.05

print(df.index.is_unique)
print(too_distant_values)
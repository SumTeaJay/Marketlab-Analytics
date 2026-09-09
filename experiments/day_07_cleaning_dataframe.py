import numpy as np 
import pandas as pd

markets_df = pd.DataFrame({
    "market_id": [1, 2, 3, 4, 5, 6, 6, 8, 9, 10, 11, 11],
    
    "demand_intercept": [
        500, 620, 450, 800, 700, 550,
        550, 900, 400, 750, np.nan, 650
    ],
    
    "demand_slope": [
        2.0, 1.5, 3.0, 2.5, np.nan, 1.0,
        1.0, 4.0, 2.0, 2.5, 1.5, 2.0
    ],
    
    "quantity": [
        100, 200, 50, 120, 100, 150,
        150, 100, 250, np.nan, 200, 200
    ],
    
    "price": [
        300, 320, 320, 500, 500, 400,
        400, 520, -100, 250, 350, 250
    ]
})

clean_markets_df = markets_df.copy()

clean_markets_df = clean_markets_df.dropna(subset=["demand_intercept", "demand_slope", "quantity", "price"])
clean_markets_df = clean_markets_df.drop_duplicates(subset=["market_id"])

clean_markets_df["price"] = pd.to_numeric(
    clean_markets_df["price"],
    errors="coerce"
)

numeric_columns = ["demand_intercept", "demand_slope", "quantity", "price"]

for column in numeric_columns:
    clean_markets_df[column] = pd.to_numeric(
    clean_markets_df[column],
    errors="coerce"
    )

clean_markets_df["price"] = clean_markets_df["demand_intercept"] - clean_markets_df["demand_slope"] * clean_markets_df["quantity"]

clean_markets_df = clean_markets_df[clean_markets_df["price"] > 0]

print(markets_df)
print("##############################################################")
print(clean_markets_df)
    
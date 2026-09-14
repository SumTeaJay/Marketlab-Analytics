import pandas as pd

df = pd.read_csv(r"data\processed\market_price_clean.csv", index_col="market_id")

print(df["quantity"].value_counts(normalize=True))
print("#" * 32)
print(df["quantity"].value_counts(normalize=False))
print("#" * 32)
print(df["quantity"].value_counts(normalize=True).sum())
print("#" * 32)
print(df["price"].agg(["mean", "median", "var", "std"]).round(2))
print("#" * 32)
df_with_higher_prices = df[df["price"] > df["price"].mean()]
print(len(df_with_higher_prices) / len(df) * 100)
print("#" * 32)
print(df.groupby("demand_slope")["price"].agg(["count", "mean", "median"]).round(2))
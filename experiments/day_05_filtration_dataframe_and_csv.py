from generate_markets import *

arrays = generate_market_parameters(100)

df = create_data_frame(arrays[0], arrays[1], arrays[2])

mean_price = np.mean(df["price"])
df_markets_higher_price = df[df["price"] >= mean_price]

df_markets_higher_price = df_markets_higher_price.sort_values("price")

df_markets_higher_price.to_csv(r"data\raw\market_price.csv")

df = pd.read_csv(r"data\raw\market_price.csv", index_col="market_id")

print(df)
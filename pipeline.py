import pandas as pd
from app import generate_markets, prepare_markets, analyze_markets

def main():
    generate_markets()
    prepare_markets()
    analyze_markets()

    prices = pd.read_csv(r"data\processed\markets_price_clean.csv")
    costs = pd.read_csv(r"data\raw\markets_costs_raw.csv")

    result = pd.merge(prices, costs, how="left", validate="one_to_one", indicator=True)
    print(result.index.is_unique)

if __name__ == "__main__":
    main()
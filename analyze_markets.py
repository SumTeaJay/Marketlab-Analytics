import pandas as pd
import matplotlib.pyplot as plt
from prepare_markets import load_markets

def main():
    df = load_markets(r"data\processed\markets_clean.csv")

    variational_series = df["quantity"].value_counts(normalize=True).sort_index()
    point_estimates = df["price"].agg(["mean", "median", "var", "std"]).round(2)
    group_units = df.groupby("demand_slope")["price"].agg(["count", "mean", "median"]).round(2)

    variational_series.to_csv(r"data\reports\quantity_variation.csv")
    point_estimates.to_csv(r"data\reports\price_estimates.csv")
    group_units.to_csv(r"data\reports\price_by_slope.csv")
    
    plt.figure()
    variational_series.plot(x="count", y="quantity", kind="bar")
    
    plt.xlabel("Q")
    plt.ylabel("Абсолютные частоты")
    plt.title("Вариационный ряд Q")

    plt.savefig(r"data\graphs\variational_series_Q.png")
    plt.close()

    plt.figure()
    df["price"].hist(bins="auto")
    
    plt.xlabel("Цена")
    plt.ylabel("Частота")
    plt.title("Гистограмма распределения цены")

    plt.savefig(r"data\graphs\price_histogram.png")
    plt.close()
if __name__ == "__main__":
    main()
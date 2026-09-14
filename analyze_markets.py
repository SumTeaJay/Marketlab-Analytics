import pandas as pd
import matplotlib.pyplot as plt
from prepare_markets import load_markets

def main():
    df = load_markets(r"data\processed\market_price_clean.csv")

    relative_frequencies = df["quantity"].value_counts(normalize=True).sort_index()
    absolute_frequencies = df["quantity"].value_counts(normalize=False).sort_index()
    point_estimates = df["price"].agg(["mean", "median", "var", "std"]).round(2)
    group_units = df.groupby("demand_slope")["price"].agg(["count", "mean", "median"]).round(2)

    relative_frequencies.to_csv(r"data\reports\relative_frequencies.csv")
    absolute_frequencies.to_csv(r"data\reports\absolute_frequencies.csv")
    point_estimates.to_csv(r"data\reports\price_estimates.csv")
    group_units.to_csv(r"data\reports\price_by_slope.csv")
    
    plt.figure()
    relative_frequencies.plot(x="count", y="quantity", kind="bar")
    
    plt.xlabel("Q")
    plt.ylabel("Относительные частоты")
    plt.title("Вариационный ряд Q")

    plt.savefig(r"data\graphs\relative_frequencies_Q.png")
    plt.close()

    plt.figure()
    absolute_frequencies.plot(x="count", y="quantity", kind="bar")
    
    plt.xlabel("Q")
    plt.ylabel("Абсолютные частоты")
    plt.title("Вариационный ряд Q")

    plt.savefig(r"data\graphs\absolute_frequencies_Q.png")
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
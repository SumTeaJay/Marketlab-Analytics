import pandas as pd
import matplotlib.pyplot as plt

def compare_prices(monopoly: pd.DataFrame, pc: pd.DataFrame):
    comparative_df = pd.DataFrame(
        {
            "market_id": monopoly["market_id"],
            "monopoly_price": monopoly["price"],
            "pc_price": pc["price"],
            "price_difference": abs(monopoly["price"] - pc["price"])
        }
    )

    mean_difference = comparative_df["price_difference"].mean()
    median_difference = comparative_df["price_difference"].median()
    return (mean_difference, median_difference)

def compare_monopoly_surpluses(monopoly: pd.DataFrame):
    mean_producers_share = (monopoly["ps"] / monopoly["sw"] * 100).mean()
    mean_consumers_share = (monopoly["cs"] / monopoly["sw"] * 100).mean()

    mean_difference = abs(monopoly["ps"] - monopoly["cs"]).mean()
    median_difference = abs(monopoly["ps"] - monopoly["cs"]).median()

    return (mean_producers_share, mean_consumers_share, mean_difference, median_difference)


def analyze_markets():
    monopoly = pd.read_csv(r"data\calculated_data\monopoly.csv")
    pc = pd.read_csv(r"data\calculated_data\perfect_competition.csv")
    print(compare_prices(monopoly, pc))
    print(compare_monopoly_surpluses(monopoly))

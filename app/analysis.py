import pandas as pd
import matplotlib.pyplot as plt

#pc - perfect competition

def create_united_df(pc: pd.DataFrame, monopoly: pd.DataFrame) -> pd.DataFrame:
    pc["regime"] = "Совершенная конкуренция"
    monopoly["regime"] = "Монополия"

    column = pc.pop('regime')
    pc.insert(0, 'regime', column)

    column = monopoly.pop('regime')
    monopoly.insert(0, 'regime', column)

    new_united_df = pd.concat([pc, monopoly])
    new_united_df = new_united_df.sort_values(by=["market_id", "regime"])
    new_united_df["difference_between_a_and_MC"] = new_united_df["demand_intercept"] - new_united_df["marginal_costs"]
    return new_united_df

def compare_prices(monopoly: pd.DataFrame, pc: pd.DataFrame):
    mean_difference = (monopoly["price"] - pc["price"]).mean()
    median_difference = (monopoly["price"] - pc["price"]).median()
    return (mean_difference, median_difference)

def compare_quantity(monopoly: pd.DataFrame, pc: pd.DataFrame):
    mean_difference = (monopoly["quantity"] - pc["quantity"]).mean()
    median_difference = (monopoly["quantity"] - pc["quantity"]).median()
    return (mean_difference, median_difference)

def return_monopoly_surpluses(monopoly: pd.DataFrame):
    mean_producers_share = monopoly["ps"].mean()
    mean_consumers_share = monopoly["cs"].mean()
    return (mean_producers_share, mean_consumers_share)

def return_pc_surpluses(pc: pd.DataFrame):
    mean_producers_share = pc["ps"].mean()
    mean_consumers_share = pc["cs"].mean()
    return (mean_producers_share, mean_consumers_share)

def return_monopoly_dwl(monopoly: pd.DataFrame):
    mean_dwl = monopoly["dwl"].mean()
    median_dwl = monopoly["dwl"].median()

    return (mean_dwl, median_dwl)

def return_markets_with_biggest_dwl(monopoly: pd.DataFrame, inverted=False):
    return monopoly.sort_values(by="dwl", ascending=inverted)[:10]

def create_graph_price_difference(monopoly: pd.DataFrame, pc: pd.DataFrame):
    plt.hist(monopoly["price"] - pc["price"], bins=20)

    plt.title("Разница между ценами монополии и совершенной конкуренции")

    plt.xlabel("Монопольная цена - цена при совершенной конкуренции")

    plt.ylabel("Количество рынков")

    plt.savefig(r"data\graphs\price_difference.png")    

def create_graph_dwl_connection_with_price(monopoly: pd.DataFrame):
    plt.scatter(
        monopoly["quantity"],
        monopoly["dwl"]
    )

    plt.xlabel("Равновесное количество")
    plt.ylabel("Общественные потери")

    plt.title("Связь между равновесным количеством и общественными потерями")

    plt.savefig(r"data\graphs\dwl_connection_with_quantity.png")

def create_report_1(pc: pd.DataFrame, monopoly: pd.DataFrame):
    with open(r"data\reports\report_1.txt", "w", encoding="utf-8") as report_file:
        print("- Данные для вопроса №1\n'Насколько в среднем и по медиане меняются цена и выпуск?'", file=report_file)
        price_differences = compare_prices(monopoly, pc)
        quantity_differences = compare_quantity(monopoly, pc)

        print(f"Средняя разница между равновесными ценами монополии и совершенной конкуренции: {price_differences[0]}", file=report_file)
        print(f"Медианная разница между равновесными ценами монополии и совершенной конкуренции: {price_differences[1]}", file=report_file)

        print(f"Средняя разница между равновесным количеством на рынке монополии и совершенной конкуренции: {quantity_differences[0]}", file=report_file)
        print(f"Медианная разница между равновесным количеством на рынке монополии и совершенной конкуренции: {quantity_differences[1]}", file=report_file)
        print(file=report_file)

        print("- Данные для вопроса №2\n'Как перераспределяется благосостояние между потребителем и производителем?'", file=report_file)

        monopoly_surpluses = return_monopoly_surpluses(monopoly)
        pc_surpluses = return_pc_surpluses(pc)

        print(f"Средний излишек производителя в монополии: {monopoly_surpluses[0]}", file=report_file)
        print(f"Средний излишек потребителя в монополии: {monopoly_surpluses[1]}", file=report_file)

        print(f"Средний излишек производителя в совершенной конкуренции: {pc_surpluses[0]}", file=report_file)
        print(f"Средний излишек потребителя в совершенной конкуренции: {pc_surpluses[1]}", file=report_file)
        print(file=report_file)
        
        print("- Данные для вопроса №3\n'3. Какова средняя и медианная величина общественных потерь?'", file=report_file)

        dwl = return_monopoly_dwl(monopoly)

        print("Общественные потери при совершенной конкуренции равны нулю", file=report_file)
        print(f"Средние общественные потери при монополии: {dwl[0]}", file=report_file)
        print(f"Медианные общественные потери при монополии: {dwl[1]}", file=report_file)

def create_report_2(pc: pd.DataFrame, monopoly: pd.DataFrame):
    pass

def analyze_markets():
    monopoly = pd.read_csv(r"data\calculated_data\monopoly.csv", index_col="market_id")
    pc = pd.read_csv(r"data\calculated_data\perfect_competition.csv", index_col="market_id")
    print(create_united_df(monopoly, pc))

    create_report_1(pc, monopoly)
    create_report_2(pc, monopoly)



import pandas as pd
import numpy as np

#pc - perfect competition

def calculate_monopoly_price(demand_intercept: np.array, marginal_cost: np.array) -> np.array:
    return (demand_intercept + marginal_cost) // 2

def calculate_monopoly_quantity(demand_intercept: np.array, demand_slope: np.array, marginal_cost: np.array) -> np.array:
    return (demand_intercept - marginal_cost) // (2 * demand_slope)

def calculate_monopoly_ps(demand_intercept: np.array, demand_slope: np.array, marginal_cost: np.array) -> np.array:
    return ((demand_intercept - marginal_cost) ** 2) // (4 * demand_slope)

def calculate_monopoly_cs(demand_intercept: np.array, demand_slope: np.array, marginal_cost: np.array) -> np.array:
    return ((demand_intercept - marginal_cost) ** 2) // (8 * demand_slope)

def calculate_monopoly_dwl(demand_intercept: np.array, demand_slope: np.array, marginal_cost: np.array) -> np.array:
    return ((demand_intercept - marginal_cost) ** 2) // (8 * demand_slope)

def calculate_pc_quantity(demand_intercept: np.array, demand_slope: np.array, marginal_cost: np.array) -> np.array:
    return (demand_intercept - marginal_cost) // demand_slope

def calculate_pc_cs(demand_intercept: np.array, demand_slope: np.array, marginal_cost: np.array) -> np.array:
    return ((demand_intercept - marginal_cost) ** 2) // (2 * demand_slope)

def create_monopoly_data_frame(market_df: pd.DataFrame) -> pd.DataFrame:
    monopoly_data_frame = pd.DataFrame({
        "price": calculate_monopoly_price(market_df["demand_intercept"], market_df["marginal_costs"]),
        "quantity": calculate_monopoly_quantity(market_df["demand_intercept"], market_df["demand_slope"], market_df["marginal_costs"]),
        "ps": calculate_monopoly_ps(market_df["demand_intercept"], market_df["demand_slope"], market_df["marginal_costs"]),
        "cs": calculate_monopoly_cs(market_df["demand_intercept"], market_df["demand_slope"], market_df["marginal_costs"]),
        "dwl": calculate_monopoly_dwl(market_df["demand_intercept"], market_df["demand_slope"], market_df["marginal_costs"]),
        "sw": calculate_monopoly_ps(market_df["demand_intercept"], market_df["demand_slope"], market_df["marginal_costs"]) + calculate_monopoly_cs(market_df["demand_intercept"], market_df["demand_slope"], market_df["marginal_costs"])
    })
    monopoly_data_frame.index.name = "market_id"
    return monopoly_data_frame

def create_pc_data_frame(market_df: pd.DataFrame) -> pd.DataFrame:
    monopoly_data_frame = pd.DataFrame({
        "price": market_df["marginal_costs"],
        "quantity": calculate_pc_quantity(market_df["demand_intercept"], market_df["demand_slope"], market_df["marginal_costs"]),
        "ps": 0,
        "cs": calculate_pc_cs(market_df["demand_intercept"], market_df["demand_slope"], market_df["marginal_costs"]),
        "dwl": 0,
        "sw": calculate_pc_cs(market_df["demand_intercept"], market_df["demand_slope"], market_df["marginal_costs"])
    })
    monopoly_data_frame.index.name = "market_id"
    return monopoly_data_frame

def validate_monopoly_and_pc(monopoly: pd.DataFrame, pc: pd.DataFrame) -> None:
    if (monopoly["price"] < pc["price"]).any():
        raise ValueError("Монопольная цена ниже конкурентной!")

    if (monopoly["ps"] < 0).any() or (monopoly["cs"] < 0).any() or (pc["ps"] < 0).any() or (pc["cs"] < 0).any():
        raise ValueError("Есть отрицательный излишек!")

    if (monopoly["sw"] > pc["sw"]).any():
        raise ValueError("Благосостояние при монополии выше чем при совершенной конкуренции!")

    if (monopoly["dwl"] < 0).any():
        raise ValueError("Общественные потери отрицательны!")
    
    if (monopoly["quantity"] < 0).any() or (pc["quantity"] < 0).any():
        raise ValueError("Равновесное количество отрицательно!")

    if (monopoly["price"] < 0).any() or (pc["price"] < 0).any():
        raise ValueError("Цена отрицательна!")

def calculate_monopoly_and_pc() -> None:
    df = pd.read_csv(r"data\processed\markets_clean.csv", index_col="market_id")

    monopoly = create_monopoly_data_frame(df)
    monopoly.to_csv(r"data\calculated_data\monopoly.csv")

    pc = create_pc_data_frame(df)
    pc.to_csv(r"data\calculated_data\perfect_competition.csv")

    validate_monopoly_and_pc(monopoly, pc)
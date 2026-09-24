import pandas as pd
import numpy as np
from app.validation import check_monopoly_and_pc, validate_monopoly_and_pc

#pc - perfect competition

def calculate_monopoly_price(demand_intercept: np.array, marginal_cost: np.array) -> np.array:
    return ((demand_intercept + marginal_cost) / 2)

def calculate_monopoly_quantity(demand_intercept: np.array, demand_slope: np.array, marginal_cost: np.array) -> np.array:
    return (demand_intercept - marginal_cost) / (2 * demand_slope)

def calculate_monopoly_ps(demand_intercept: np.array, demand_slope: np.array, marginal_cost: np.array) -> np.array:
    return (((demand_intercept - marginal_cost) ** 2) / (4 * demand_slope))

def calculate_monopoly_cs(demand_intercept: np.array, demand_slope: np.array, marginal_cost: np.array) -> np.array:
    return (((demand_intercept - marginal_cost) ** 2) / (8 * demand_slope))

def calculate_monopoly_dwl(demand_intercept: np.array, demand_slope: np.array, marginal_cost: np.array) -> np.array:
    return np.round(((demand_intercept - marginal_cost) ** 2) / (8 * demand_slope), 2)

def calculate_pc_quantity(demand_intercept: np.array, demand_slope: np.array, marginal_cost: np.array) -> np.array:
    return (demand_intercept - marginal_cost) / demand_slope

def calculate_pc_cs(demand_intercept: np.array, demand_slope: np.array, marginal_cost: np.array) -> np.array:
    return ((demand_intercept - marginal_cost) ** 2) / (2 * demand_slope)

def create_monopoly_data_frame(market_df: pd.DataFrame) -> pd.DataFrame:
    cs = calculate_monopoly_cs(market_df["demand_intercept"], market_df["demand_slope"], market_df["marginal_costs"])
    ps = calculate_monopoly_ps(market_df["demand_intercept"], market_df["demand_slope"], market_df["marginal_costs"])
    monopoly_data_frame = pd.DataFrame({
        "demand_intercept": market_df["demand_intercept"],
        "demand_slope": market_df["demand_slope"],
        "marginal_costs": market_df["marginal_costs"],
        "price": calculate_monopoly_price(market_df["demand_intercept"], market_df["marginal_costs"]),
        "quantity": calculate_monopoly_quantity(market_df["demand_intercept"], market_df["demand_slope"], market_df["marginal_costs"]),
        "ps": ps,
        "cs": cs,
        "dwl": calculate_monopoly_dwl(market_df["demand_intercept"], market_df["demand_slope"], market_df["marginal_costs"]),
        "sw": ps + cs
    })
    monopoly_data_frame.index.name = "market_id"
    return monopoly_data_frame

def create_pc_data_frame(market_df: pd.DataFrame) -> pd.DataFrame:
    monopoly_data_frame = pd.DataFrame({
        "demand_intercept": market_df["demand_intercept"],
        "demand_slope": market_df["demand_slope"],
        "marginal_costs": market_df["marginal_costs"],
        "price": market_df["marginal_costs"],
        "quantity": calculate_pc_quantity(market_df["demand_intercept"], market_df["demand_slope"], market_df["marginal_costs"]),
        "ps": 0,
        "cs": calculate_pc_cs(market_df["demand_intercept"], market_df["demand_slope"], market_df["marginal_costs"]),
        "dwl": 0,
        "sw": calculate_pc_cs(market_df["demand_intercept"], market_df["demand_slope"], market_df["marginal_costs"])
    })
    monopoly_data_frame.index.name = "market_id"
    return monopoly_data_frame

def calculate_monopoly_and_pc() -> None:
    initial_dataframe = pd.read_csv(r"data\processed\markets_clean.csv", index_col="market_id")

    monopoly = create_monopoly_data_frame(initial_dataframe)
    monopoly.to_csv(r"data\calculated_data\monopoly.csv")

    pc = create_pc_data_frame(initial_dataframe)
    pc.to_csv(r"data\calculated_data\perfect_competition.csv")

    validate_monopoly_and_pc(monopoly, pc)
    check_monopoly_and_pc(monopoly, pc, initial_dataframe)

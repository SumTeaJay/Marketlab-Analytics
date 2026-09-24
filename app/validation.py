import pandas as pd
import numpy as np

def validate_market_id(pc: pd.DataFrame, monopoly: pd.DataFrame, initial_dataframe: pd.DataFrame) -> bool:
    return (pc.index == monopoly.index).all() and ((monopoly.index == initial_dataframe.index)).all() and ((pc.index == initial_dataframe.index)).all()

def validate_market_parameters(pc: pd.DataFrame, monopoly: pd.DataFrame, initial_dataframe: pd.DataFrame) -> bool:
    is_a_same = (pc["demand_intercept"] == monopoly["demand_intercept"]).all() and (monopoly["demand_intercept"] == initial_dataframe["demand_intercept"]).all() and (pc["demand_intercept"] == initial_dataframe["demand_intercept"]).all()
    is_b_same = (pc["demand_slope"] == monopoly["demand_slope"]).all() and (monopoly["demand_slope"] == initial_dataframe["demand_slope"]).all() and (pc["demand_slope"] == initial_dataframe["demand_slope"]).all()
    is_MC_same = (pc["marginal_costs"] == monopoly["marginal_costs"]).all() and (monopoly["marginal_costs"] == initial_dataframe["marginal_costs"]).all() and (pc["marginal_costs"] == initial_dataframe["marginal_costs"]).all()
    return is_a_same and is_b_same and is_MC_same

def validate_market_quantity(pc: pd.DataFrame, monopoly: pd.DataFrame):
    return (pc["quantity"] == 2 * monopoly["quantity"]).all()

def validate_sw(pc: pd.DataFrame, monopoly: pd.DataFrame):
    return np.allclose(monopoly["sw"] + monopoly["dwl"], pc["sw"], 2)

def validate_values(pc: pd.DataFrame, monopoly: pd.DataFrame):
    if pc.isna().any().any() == True:
        raise ValueError("Пустые данные в таблице совершенной конкуренции!")

    if np.isinf(pc).any().any() == True:
        raise ValueError("Бесконечные данные в таблице совершенной конкуренции!")

    if monopoly.isna().any().any() == True:
        raise ValueError("Пустые данные в таблице монополии!")

    if np.isinf(monopoly).any().any() == True:
        raise ValueError("Бесконечные данные в таблице монополии!")

def check_monopoly_equality(monopoly: pd.DataFrame):
    return (monopoly["sw"] == monopoly["cs"] + monopoly["ps"]).all()

def check_pc_equality(pc: pd.DataFrame):
    return (pc["sw"] == pc["cs"] + pc["ps"]).all()

def check_monopoly_and_pc(monopoly: pd.DataFrame, pc: pd.DataFrame, initial_dataframe: pd.DataFrame):
    if not validate_market_id(pc, monopoly, initial_dataframe):
        raise ValueError("Разные market_id в таблицах!")

    if not validate_market_parameters(pc, monopoly, initial_dataframe):
        raise ValueError("Разные параметры a, b, MC в таблицах!")

    if not validate_sw(pc, monopoly):
        raise ValueError("Не выполняется равенство SW(мон) + DWL == SW(ск)")

    if not validate_market_quantity(pc, monopoly):
        raise ValueError("Не выполняется равенство SW(мон) + DWL == SW(ск)")  

    if not check_monopoly_equality(monopoly):
        raise ValueError("У монополий не выполняется равенство CS + PS = SW") 

    if not check_pc_equality(pc):
        raise ValueError("У совершенной конкуренции не выполняется равенство CS + PS = SW") 

    validate_values(pc, monopoly)

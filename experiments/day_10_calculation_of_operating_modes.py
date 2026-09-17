import pandas as pd
import numpy as np

orders = pd.DataFrame({
    "order_id": [
        "ORD-001",
        "ORD-002",
        "ORD-003",
        "ORD-004",
        "ORD-005",
        "ORD-006",
        "ORD-007",
        "ORD-008",
        "ORD-009",
        "ORD-010",
        "ORD-011",
        "ORD-012"
    ],
    "distance_km": [
        0.1,
        5.0,
        12.4,
        22.0,
        22.00000001,
        21.99999999,
        29.0,
        18.0,
        35.0,
        8.5,
        50.0,
        16.75
    ],
    "weight_kg": [
        1.0,
        2.5,
        3.2,
        4.0,
        4.0,
        4.0,
        8.0,
        6.0,
        5.0,
        10.0,
        12.0,
        1.0
    ]
})

tariff_a = {
    "fixed": 120.1,
    "per_km": 18.2,
    "per_kg": 35.3
}

tariff_b = {
    "fixed": 180.1,
    "per_km": 14.2,
    "per_kg": 42.3
}

orders_price_a = tariff_a["fixed"] + tariff_a["per_km"] * orders["distance_km"] + tariff_a["per_kg"] * orders["weight_kg"]
orders_price_b = tariff_b["fixed"] + tariff_b["per_km"] * orders["distance_km"] + tariff_b["per_kg"] * orders["weight_kg"]

cheaper_orders = np.minimum(orders_price_a, orders_price_b)

print("Стоимость заказов по тарифу А и Б")
print(orders_price_a[:5])
print(orders_price_b[:5])

print("Стоимость заказов по наиболее дешевым тарифам")
print(cheaper_orders[:5])

print("Проверка неотрицательности стоимостей")
print(orders_price_a >= 0)
print(orders_price_b >= 0)

print("Альтернативная проверка стоимости тарифов")
orders_price_alternate = pd.DataFrame({
    "tariff_a": [
        tariff_a["fixed"] + orders["distance_km"][0] * tariff_a["per_km"] + orders["weight_kg"][0] * tariff_a["per_kg"],
        tariff_a["fixed"] + orders["distance_km"][1] * tariff_a["per_km"] + orders["weight_kg"][1] * tariff_a["per_kg"],
        tariff_a["fixed"] + orders["distance_km"][2] * tariff_a["per_km"] + orders["weight_kg"][2] * tariff_a["per_kg"],
        tariff_a["fixed"] + orders["distance_km"][3] * tariff_a["per_km"] + orders["weight_kg"][3] * tariff_a["per_kg"],
        tariff_a["fixed"] + orders["distance_km"][4] * tariff_a["per_km"] + orders["weight_kg"][4] * tariff_a["per_kg"]
    ],
    "tariff_b": [
            tariff_b["fixed"] + orders["distance_km"][0] * tariff_b["per_km"] + orders["weight_kg"][0] * tariff_b["per_kg"],
            tariff_b["fixed"] + orders["distance_km"][1] * tariff_b["per_km"] + orders["weight_kg"][1] * tariff_b["per_kg"],
            tariff_b["fixed"] + orders["distance_km"][2] * tariff_b["per_km"] + orders["weight_kg"][2] * tariff_b["per_kg"],
            tariff_b["fixed"] + orders["distance_km"][3] * tariff_b["per_km"] + orders["weight_kg"][3] * tariff_b["per_kg"],
            tariff_b["fixed"] + orders["distance_km"][4] * tariff_b["per_km"] + orders["weight_kg"][4] * tariff_b["per_kg"]
    ]
})

print(np.isclose(orders_price_a[:5], orders_price_alternate["tariff_a"]))
print(np.isclose(orders_price_b[:5], orders_price_alternate["tariff_b"]))

print("Заказы, для которых стоимости почти равны")
print(orders_price_a[np.isclose(orders_price_a, orders_price_b)])
import numpy as np

prices = np.array([19.99, 35.50, 12.75, 44.40, 28.30])
quantity = np.array([3, 2, 5, 1, 4])

discount = 0.15   # скидка 15%
tax = 0.20        # налог 20%

print("Два способа без округления стоимости")
subtotal = np.sum(prices * quantity)

total_cost_1 = subtotal * (1 - discount) * (1 + tax)
total_cost_2 = np.sum(prices * quantity * (1 - discount) * (1 + tax))

print(total_cost_1 == total_cost_2)
print(np.allclose(total_cost_1, total_cost_2))

print("Округление стоимости со скидкой")
total_cost_3 = ((prices * quantity) * (1 - discount)).round(2) + tax * (prices * quantity)
print(total_cost_1 == total_cost_3)
print(np.allclose(total_cost_1, total_cost_3))
import pandas as pd

# Каталог книг: каждый book_id уникален
books = pd.DataFrame({
    "book_id": [101, 102, 103, 104],
    "title": [
        "Мастер и Маргарита",
        "Преступление и наказание",
        "1984",
        "Маленький принц"
    ],
    "price": [750, 900, 650, 500]
})

# Продажи: один book_id может встречаться несколько раз
sales = pd.DataFrame({
    "sale_id": [1, 2, 3, 4, 5, 6, 7],
    "book_id": [101, 103, 101, 102, 103, 101, 105],
    "quantity": [1, 2, 1, 3, 1, 2, 4]
})

result = pd.merge(sales, books, how="left", on="book_id", validate="many_to_one", indicator=True)
print(result)
print(result[result["_merge"]=="left_only"])
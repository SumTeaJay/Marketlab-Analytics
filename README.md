# Marketlab-Analytics
## Что это за проект
Это учебная платформа для исследования рыночной конкуренции.

## Требования
Python 3.14+

## Установка
Перейдите в папку, куда хотите установить проект, указав полный путь:
```bash
cd C:\Users\example
```

Клонируйте репозиторий:
```bash
git clone https://github.com/SumTeaJay/Marketlab-Analytics.git
```


## Запуск
Введите следующую команду:

```bash
python generate_markets.py
```

**NB!** Если вы запускаете упражнения, перейдите в корень проекта и введите следующую команду:
```bash
python -m experiments.name.py
```

## Структура
```text
Marketlab-Analytics/
├── experiments/
├── data/
│   └── raw/
│       └── markets.csv
├── main.py
└── README.md
```

- `experiments/` — скрипты и описание упражнений по дням.
- `data/raw/markets.csv` — данные о рынках, рассчитанные по формуле P = a - b * Q
- `generate_markets.py` — основной скрипт генерации рынков.
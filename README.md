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

Создайте виртуальное окружение:
```bash
python -m venv .venv
```

Активируйте его в PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```

Установите зависимости для разработки:
```bash
pip install -r requirements.txt
```

## Запуск
Сначала сгенерируйте данные:

```bash
python generate_markets.py
```

Затем очистите их:
```bash
python prepare_markets.py
```

Потом проанализируйте их:
```bash
python analyze_markets.py
```

**NB!** Если вы запускаете упражнения, перейдите в корень проекта и введите следующую команду:
```bash
python -m experiments.name
```

## Структура
- `experiments/` — скрипты и описание упражнений по дням.
- `data/raw/market_price.csv` — сырые данные о рынках, рассчитанные по формуле P = a - b * Q
- `data/processed/market_price_clean.csv` — обработанные данные о рынках
- `data/reports` — данные, проанализированные с помощью статистических методов
- `generate_markets.py` — основной скрипт генерации рынков.
- `prepare_markets.py` — скрипт очистки данных.
- `analyze_markets.py` — скрипт анализа данных рынков с помощью статистических задач.
- `requirements.txt` — необходимые библиотеки для установки
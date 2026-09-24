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
Запустите процесс анализа:

```bash
python pipeline.py
```


**NB!** Если вы запускаете упражнения, перейдите в корень проекта и введите следующую команду:
```bash
python -m experiments.name
```

## Структура
- `experiments/` — скрипты и описание упражнений по дням.
- `data/raw/` — сгенерированные данные о рынках
- `data/processed/` — обработанные данные о рынках
- `data/audit/` — найденные ошибки в данных
- `data/calculated_data/` — модели рынков и их параметры
- `data/graphs/` — графики
- `pipeline.py` — основной скрипт, запускающий анализ
- `app/` — скрипты-этапы анализа
- `documentation/` — документы для работы
- `notes/` — общие впечатления от работы на неделе
- `requirements.txt` — необходимые библиотеки для установки
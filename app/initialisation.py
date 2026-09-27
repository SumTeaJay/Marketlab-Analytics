from pathlib import Path

def create_data_dirs(dir_name: str) -> None:
    PROJECT_DIR = Path(__file__).resolve().parent.parent
    DATA_DIR = PROJECT_DIR / "data"
    DATA_DIR.mkdir(exist_ok=True)
    CREATED_DIR = DATA_DIR / dir_name
    CREATED_DIR.mkdir(exist_ok=True, parents=True)
    return CREATED_DIR
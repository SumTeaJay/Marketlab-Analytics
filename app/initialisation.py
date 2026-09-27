from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_DIR / "data"

RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
CALCULATED_DIR = DATA_DIR / "calculated"
GRAPHS_DIR = DATA_DIR / "graphs"
AUDIT_DIR = DATA_DIR / "audit"
REPORTS_DIR = DATA_DIR / "reports"

def create_data_dirs():
    for directory in [DATA_DIR, RAW_DIR, PROCESSED_DIR, CALCULATED_DIR, GRAPHS_DIR, AUDIT_DIR, REPORTS_DIR]:
        directory.mkdir(exist_ok=True, parents=True)
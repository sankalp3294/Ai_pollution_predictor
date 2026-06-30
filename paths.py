from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent
DATA_DIR = ROOT_DIR / "data"

RAW_DATASET_PATH = DATA_DIR / "dataset.csv"
CLEAN_DATASET_PATH = DATA_DIR / "clean_dataset.csv"
CITY_DAY_DATASET_PATH = DATA_DIR / "city_day.csv"
MODEL_PATH = ROOT_DIR / "ai_pollution_model.pkl"

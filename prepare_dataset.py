import pandas as pd

from model import MODEL_COLUMNS
from paths import CLEAN_DATASET_PATH, RAW_DATASET_PATH


if __name__ == "__main__":
    df = pd.read_csv(RAW_DATASET_PATH)

    print("Original shape:", df.shape)

    df = df[MODEL_COLUMNS].dropna().drop_duplicates()

    print("Clean shape:", df.shape)

    df.to_csv(CLEAN_DATASET_PATH, index=False)

    print(f"Dataset cleaned successfully: {CLEAN_DATASET_PATH}")

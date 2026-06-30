import joblib
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

from paths import CLEAN_DATASET_PATH, MODEL_PATH, RAW_DATASET_PATH


FEATURE_COLUMNS = ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]
TARGET_COLUMN = "AQI"
MODEL_COLUMNS = FEATURE_COLUMNS + [TARGET_COLUMN]


def load_training_dataset() -> pd.DataFrame:
    dataset_path = CLEAN_DATASET_PATH if CLEAN_DATASET_PATH.exists() else RAW_DATASET_PATH
    return pd.read_csv(dataset_path)[MODEL_COLUMNS].dropna().drop_duplicates()


def build_model() -> HistGradientBoostingRegressor:
    return HistGradientBoostingRegressor(
        learning_rate=0.08,
        max_depth=10,
        max_iter=250,
        min_samples_leaf=20,
        random_state=42,
    )


def train_and_save_model() -> dict:
    df = load_training_dataset()
    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    model = build_model()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    metrics = {
        "r2": r2_score(y_test, predictions),
        "mae": mean_absolute_error(y_test, predictions),
        "rows": len(df),
    }

    joblib.dump(model, MODEL_PATH, compress=3)
    return metrics


def load_model():
    return joblib.load(MODEL_PATH)

# Air Quality Index (AQI) Predictor

A Streamlit app that predicts AQI from six pollutant inputs using a trained scikit-learn regression model.

## Project Layout

```text
AI_Agent_Pollution_Improved/
|-- app.py
|-- model.py
|-- paths.py
|-- train_model.py
|-- prepare_dataset.py
|-- utils.py
|-- requirements.txt
|-- data/
|   |-- dataset.csv
|   |-- city_day.csv
|   |-- station_day.csv
|   |-- station_hour.csv
|   `-- stations.csv
`-- ai_pollution_model.pkl
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Generate the cleaned dataset

```bash
python prepare_dataset.py
```

This writes `data/clean_dataset.csv`.

## Train the model

```bash
python train_model.py
```

This reads from `data/clean_dataset.csv` when available, otherwise it falls back to `data/dataset.csv`, and writes `ai_pollution_model.pkl`.

## Run the app

```bash
streamlit run app.py
```

## Deploy Notes

- Keep large raw data files under `data/`.
- `data/clean_dataset.csv` is treated as generated output and ignored by Git.
- The model is rebuilt with `HistGradientBoostingRegressor` so the artifact stays small enough for normal Git hosting and Streamlit-style deployment.

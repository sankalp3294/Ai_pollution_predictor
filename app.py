import numpy as np
import pandas as pd
import streamlit as st

from model import FEATURE_COLUMNS, load_model
from paths import MODEL_PATH
from utils import aqi_category, aqi_description


st.set_page_config(page_title="AQI Predictor", page_icon="AQI", layout="wide")
st.title("Air Quality Index Predictor")


@st.cache_resource
def get_model():
    return load_model()


try:
    model = get_model()
except Exception as exc:
    st.error(f"Model loading failed: {exc}")
    if not MODEL_PATH.exists():
        st.info("Run `python train_model.py` once to create the model file before starting the app.")
    st.stop()


with st.sidebar:
    st.header("Pollutant Inputs")
    pm25 = st.number_input("PM2.5", 0.0, 500.0, 40.0)
    pm10 = st.number_input("PM10", 0.0, 600.0, 80.0)
    no2 = st.number_input("NO2", 0.0, 300.0, 25.0)
    so2 = st.number_input("SO2", 0.0, 300.0, 12.0)
    co = st.number_input("CO", 0.0, 30.0, 0.8)
    o3 = st.number_input("O3", 0.0, 300.0, 35.0)


if st.button("Predict AQI"):
    data = pd.DataFrame(
        np.array([[pm25, pm10, no2, so2, co, o3]]),
        columns=FEATURE_COLUMNS,
    )
    aqi = float(model.predict(data)[0])
    category = aqi_category(aqi)

    st.metric("Predicted AQI", f"{aqi:.1f}")
    st.success(category)
    st.info(aqi_description(category))

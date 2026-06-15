# 🌿 Air Quality Index (AQI) Predictor

An intelligent machine learning application that predicts Air Quality Index based on pollutant concentrations. Built with Streamlit for easy web-based access and interactive predictions.

## 📋 Overview

This project leverages a trained machine learning model to predict AQI values based on six key air pollutants. The application provides real-time predictions with AQI categorization and health impact descriptions.

## ✨ Features

- **Real-time AQI Prediction**: Get instant AQI forecasts based on pollutant levels
- **6 Pollutant Inputs**: PM2.5, PM10, NO2, SO2, CO, and O3
- **AQI Categorization**: Automatic classification (Good, Moderate, Poor, Severe, etc.)
- **Health Descriptions**: Contextual information about air quality impact
- **User-Friendly Interface**: Interactive Streamlit dashboard
- **Cached Model Loading**: Optimized performance with resource caching

## 🛠️ Prerequisites

- Python 3.7+
- pip package manager

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd AI_Agent_Pollution_Improved
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### How to Use:

1. Adjust pollutant concentration values in the left sidebar
2. Click the **"Predict AQI"** button
3. View the predicted AQI score, category, and health recommendations

## 📁 Project Structure

```
AI_Agent_Pollution_Improved/
├── app.py                      # Main Streamlit application
├── utils.py                    # Utility functions (AQI categorization & descriptions)
├── requirements.txt            # Python dependencies
├── ai_pollution_model.pkl      # Trained machine learning model
├── README.md                   # Project documentation
└── .gitignore                  # Git ignore rules
```

## 🎯 Input Parameters

| Pollutant | Range | Unit | Description |
|-----------|-------|------|-------------|
| PM2.5 | 0-500 | µg/m³ | Fine particulate matter |
| PM10 | 0-600 | µg/m³ | Coarse particulate matter |
| NO2 | 0-300 | ppb | Nitrogen dioxide |
| SO2 | 0-300 | ppb | Sulfur dioxide |
| CO | 0-30 | ppm | Carbon monoxide |
| O3 | 0-300 | ppb | Ozone |

## 📊 Output

The application returns:
- **AQI Score**: Numerical value (0-500+)
- **AQI Category**: Good, Moderate, Poor, Very Poor, or Severe
- **Health Advisory**: Recommendations based on air quality level

## 🔧 Dependencies

- **streamlit** - Web app framework
- **joblib** - Model serialization and loading
- **numpy** - Numerical computations
- **scikit-learn** - Machine learning model

## ⚙️ Configuration

Model file location: `ai_pollution_model.pkl`

Ensure the model file is in the project root directory.

## 📝 License

This project is provided as-is for educational and research purposes.

---

**For issues or improvements, please open an issue or submit a pull request!**

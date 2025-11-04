import pandas as pd
import joblib
from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

HISTORICAL_FILE = DATA_DIR / "historical.csv"
MODEL_FILE = DATA_DIR / "model.pkl"

def load_data():
    if HISTORICAL_FILE.exists():
        return pd.read_csv(HISTORICAL_FILE)
    return pd.DataFrame()

def save_data(df):
    df.to_csv(HISTORICAL_FILE, index=False)

def load_model():
    if MODEL_FILE.exists():
        return joblib.load(MODEL_FILE)
    return None

def save_model(model):
    joblib.dump(model, MODEL_FILE)

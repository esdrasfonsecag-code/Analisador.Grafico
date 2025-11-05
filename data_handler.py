import pandas as pd
import joblib
from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
print("[data_handler] Pasta de dados pronta:", DATA_DIR)

HISTORICAL_FILE = DATA_DIR / "historical.csv"
MODEL_FILE = DATA_DIR / "model.pkl"

def load_data():
    if HISTORICAL_FILE.exists():
        try:
            return pd.read_csv(HISTORICAL_FILE, encoding="utf-8")
        except Exception as e:
            print(f"[data_handler] Erro ao carregar dados: {e}")
            return pd.DataFrame()
    return pd.DataFrame()

def save_data(df):
    temp_file = HISTORICAL_FILE.with_suffix(".tmp")
    df.to_csv(temp_file, index=False, encoding="utf-8")
    temp_file.replace(HISTORICAL_FILE)

def load_model():
    if MODEL_FILE.exists():
        try:
            return joblib.load(MODEL_FILE)
        except Exception as e:
            print(f"[data_handler] Erro ao carregar modelo: {e}")
            return None
    return None

def save_model(model):
    joblib.dump(model, MODEL_FILE)

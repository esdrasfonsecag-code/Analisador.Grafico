from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np

from model import FootballAIPro
from data_handler import load_data, save_data
from features import prepare_features
from visualization import plot_heatmap, plot_probabilities

app = FastAPI()
ai = FootballAIPro()

class MatchData(BaseModel):
    gols_time_a: int
    gols_time_b: int
    result: int  # 0 = under 2.5, 1 = over 2.5

@app.post("/update")
def update(data: MatchData):
    df = load_data()
    
    # Adiciona nova partida
    new_row = {
        'gols_time_a': data.gols_time_a,
        'gols_time_b': data.gols_time_b,
        'gols_total': data.gols_time_a + data.gols_time_b,
        'result': data.result
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    save_data(df)
    
    # Prepara features
    features = prepare_features(df)
    X_new = features.tail(10).values
    y_new = df['result'].tail(10).values

    # Atualiza modelo
    ai.update_model(X_new, y_new)

    # Gráficos
    plot_heatmap(features)
    probs = ai.predict(features.values)
    plot_probabilities(df, probs)

    return {"status": "model updated", "prob_over_latest": float(probs[-1])}

@app.post("/predict")
def predict(data: MatchData):
    df = load_data()
    
    # Adiciona partida futura
    df_future = pd.concat([df, pd.DataFrame([{
        'gols_time_a': data.gols_time_a,
        'gols_time_b': data.gols_time_b,
        'gols_total': data.gols_time_a + data.gols_time_b
    }])], ignore_index=True)
    
    features = prepare_features(df_future)
    X_pred = features.values[-1].reshape(1, -1)
    
    prob = ai.predict(X_pred)[0]
    return {"probability_over_2.5": float(prob)}

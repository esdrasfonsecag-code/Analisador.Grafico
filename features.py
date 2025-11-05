import pandas as pd

def prepare_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Criação de features avançadas para maior assertividade na previsão de gols.
    """
    if df.empty:
        print("[features] DataFrame vazio — nenhuma feature gerada.")
        return df

    required_cols = ['gols_time_a', 'gols_time_b', 'result', 'gols_total']
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"[features] Coluna ausente: {col}")

    # Médias móveis
    df['media_gols_time_a'] = df['gols_time_a'].rolling(5, min_periods=1).mean()
    df['media_gols_time_b'] = df['gols_time_b'].rolling(5, min_periods=1).mean()
    df['dif_media_gols'] = df['media_gols_time_a'] - df['media_gols_time_b']

    # Sequência de over/under recentes
    df['seq_over'] = df['result'].rolling(5, min_periods=1).sum()

    # Média de gols totais recentes
    df['media_gols_total'] = df['gols_total'].rolling(5, min_periods=1).mean()

    # Normalização leve (opcional)
    for col in ['media_gols_time_a', 'media_gols_time_b', 'media_gols_total']:
        df[col] = (df[col] - df[col].mean()) / (df[col].std() + 1e-6)

    # Seleciona features
    features = df[['media_gols_time_a', 'media_gols_time_b', 'dif_media_gols', 'seq_over', 'media_gols_total']]

    print(f"[features] Features geradas com sucesso: {len(features)} linhas.")
    return features.fillna(0)

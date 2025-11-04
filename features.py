def prepare_features(df):
    """
    Criação de features avançadas para maior assertividade.
    """
    # Médias móveis
    df['media_gols_time_a'] = df['gols_time_a'].rolling(5, min_periods=1).mean()
    df['media_gols_time_b'] = df['gols_time_b'].rolling(5, min_periods=1).mean()
    df['dif_media_gols'] = df['media_gols_time_a'] - df['media_gols_time_b']

    # Sequência de over/under
    df['seq_over'] = df['result'].rolling(5, min_periods=1).sum()

    # Média de gols totais recentes
    df['media_gols_total'] = df['gols_total'].rolling(5, min_periods=1).mean()

    # Seleciona features
    features = df[['media_gols_time_a','media_gols_time_b','dif_media_gols','seq_over','media_gols_total']]
    return features.fillna(0)

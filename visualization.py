import matplotlib
matplotlib.use('Agg')  # Importante para Render: evita erro "no display name"
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def plot_heatmap(df):
    """Gera e salva um mapa de calor das correlações."""
    plt.figure(figsize=(8, 6))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title("Correlação das Features")
    plt.tight_layout()
    plt.savefig(DATA_DIR / "heatmap_features.png")
    plt.close()

def plot_probabilities(df, probs):
    """Plota a probabilidade de over 2.5 em linha temporal."""
    plt.figure(figsize=(8, 6))
    df_plot = df.copy()
    df_plot['prob_over'] = probs
    sns.lineplot(x=range(len(df_plot)), y='prob_over', data=df_plot)
    plt.title("Probabilidade de Over 2.5")
    plt.xlabel("Jogos")
    plt.ylabel("Probabilidade")
    plt.tight_layout()
    plt.savefig(DATA_DIR / "probs_line.png")
    plt.close()

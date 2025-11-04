import matplotlib.pyplot as plt
import seaborn as sns

def plot_heatmap(df):
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title("Correlação das Features")
    plt.savefig("data/heatmap_features.png")
    plt.close()

def plot_probabilities(df, probs):
    df_plot = df.copy()
    df_plot['prob_over'] = probs
    sns.lineplot(x=range(len(df_plot)), y='prob_over', data=df_plot)
    plt.title("Probabilidade de Over 2.5")
    plt.savefig("data/probs_line.png")
    plt.close()

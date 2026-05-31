import seaborn as sns
import matplotlib.pyplot as plt

from scipy.stats import spearmanr

def correlation_analysis(df):

    plt.style.use('ggplot')

    # SPEARMAN CORRELATION

    x = df['Deaths']

    y = df['Confirmed']

    correlation, p_value = spearmanr(x, y)

    print("\nSPEARMAN CORRELATION\n")

    print("Correlation Coefficient =", correlation)

    print("P-value =", p_value)

    # CORRELATION MATRIX

    corr_matrix = df.corr(numeric_only=True)

    print("\nCORRELATION MATRIX\n")

    print(corr_matrix)

    # HEATMAP

    plt.figure(figsize=(10,8))

    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap='coolwarm'
    )

    plt.title(
        "Correlation Heatmap",
        fontsize=16
    )

    plt.tight_layout()

    plt.show()
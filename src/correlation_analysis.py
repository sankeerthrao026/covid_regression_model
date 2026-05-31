import seaborn as sns
import matplotlib.pyplot as plt

from scipy.stats import spearmanr

def correlation_analysis(df):

    x = df['Deaths']
    y = df['Confirmed']

    correlation, p_value = spearmanr(x, y)

    print("\nSPEARMAN CORRELATION\n")

    print("Correlation Coefficient =", correlation)

    print("P-value =", p_value)

    # Correlation Matrix
    corr_matrix = df.corr(numeric_only=True)

    print("\nCORRELATION MATRIX\n")
    print(corr_matrix)

    # Heatmap
    plt.figure(figsize=(10,8))

    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap='coolwarm'
    )

    plt.title("Correlation Heatmap")

    plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def clean_data():

    df = pd.read_csv("dataset/covid_data.csv")

    print("\nFIRST 5 ROWS\n")

    print(df.head())

    print("\nMISSING VALUES\n")

    print(df.isnull().sum())

    # HANDLE MISSING VALUES
    df.fillna(0, inplace=True)

    # REMOVE DUPLICATES
    df.drop_duplicates(inplace=True)

    # CONVERT DATE TYPE
    df['Date'] = pd.to_datetime(df['Date'])

    print("\nDATASET INFO\n")

    print(df.info())

    # OUTLIER DETECTION
    plt.style.use('ggplot')

    plt.figure(figsize=(8,6))

    sns.boxplot(
        x=df['Confirmed']
    )

    plt.title("Outlier Detection")

    plt.tight_layout()

    plt.show()

    return df
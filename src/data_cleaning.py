import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def clean_data():

    df = pd.read_csv("dataset/covid_data.csv")

    print("\nFIRST 5 ROWS\n")
    print(df.head())

    print("\nMISSING VALUES\n")
    print(df.isnull().sum())

    # Fill Missing Values
    df.fillna(0, inplace=True)

    # Remove Duplicates
    df.drop_duplicates(inplace=True)

    # Convert Date
    df['Date'] = pd.to_datetime(df['Date'])

    print("\nDATASET INFO\n")
    print(df.info())

    # Outlier Detection
    plt.figure(figsize=(8,6))

    sns.boxplot(df['Confirmed'])

    plt.title("Outlier Detection")

    plt.show()

    return df
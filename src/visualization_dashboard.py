import matplotlib.pyplot as plt

def visualization_dashboard(df):

    # LINE GRAPH
    plt.figure(figsize=(10,6))

    plt.plot(df['Date'], df['Confirmed'])

    plt.title("Confirmed Cases Over Time")

    plt.xlabel("Date")

    plt.ylabel("Confirmed Cases")

    plt.xticks(rotation=45)

    plt.show()

    # BAR CHART
    country_cases = df.groupby(
        'Country'
    )['Confirmed'].sum()

    country_cases.plot(kind='bar')

    plt.title("Country-wise Cases")

    plt.show()

    # HISTOGRAM
    plt.hist(df['Active'])

    plt.title("Active Cases Distribution")

    plt.xlabel("Active Cases")

    plt.ylabel("Frequency")

    plt.show()
import matplotlib.pyplot as plt

def visualization_dashboard(df):

    plt.style.use('ggplot')

    # =====================================
    # COUNTRY-WISE CASES
    # =====================================

    country_cases = df.groupby(
        'Country'
    )['Confirmed'].sum()

    plt.figure(figsize=(10,6))

    country_cases.sort_values(
        ascending=False
    ).plot(
        kind='bar'
    )

    plt.title(
        "Country-wise COVID Cases",
        fontsize=16
    )

    plt.xlabel("Country")

    plt.ylabel("Confirmed Cases")

    plt.tight_layout()

    plt.show()

    # =====================================
    # ACTIVE CASES HISTOGRAM
    # =====================================

    plt.figure(figsize=(8,6))

    plt.hist(
        df['Active'],
        bins=10
    )

    plt.title(
        "Active Cases Distribution",
        fontsize=16
    )

    plt.xlabel("Active Cases")

    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.show()
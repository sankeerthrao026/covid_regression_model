import matplotlib.pyplot as plt

def trend_analysis(df):

    plt.style.use('ggplot')

    countries = df['Country'].unique()

    # =====================================
    # CONFIRMED TREND
    # =====================================

    plt.figure(figsize=(12,6))

    for country in countries:

        country_data = df[
            df['Country'] == country
        ]

        plt.plot(
            country_data['Date'],
            country_data['Confirmed'],
            marker='o',
            linewidth=2,
            label=country
        )

    plt.title(
        "COVID-19 Confirmed Cases Trend",
        fontsize=16
    )

    plt.xlabel("Date")

    plt.ylabel("Confirmed Cases")

    plt.xticks(rotation=45)

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    plt.show()
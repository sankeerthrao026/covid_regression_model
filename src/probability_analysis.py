def probability_analysis(df):

    recovery_probability = (
        df['Recovered'].sum()
        /
        df['Confirmed'].sum()
    )

    death_probability = (
        df['Deaths'].sum()
        /
        df['Confirmed'].sum()
    )

    print("\nRECOVERY PROBABILITY =")
    print(recovery_probability)

    print("\nDEATH PROBABILITY =")
    print(death_probability)
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

def regression_model(df):

    plt.style.use('ggplot')

    # FEATURES

    X = df[
        ['Deaths',
         'Recovered',
         'Active',
         'Vaccinated']
    ]

    # TARGET

    y = df['Confirmed']

    # SPLIT DATASET

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # CREATE MODEL

    model = LinearRegression()

    # =====================================
    # TRAIN MODEL
    # =====================================

    model.fit(X_train, y_train)

    print("\nMODEL TRAINED SUCCESSFULLY")

    # PREDICTIONS

    y_pred = model.predict(X_test)

    # EVALUATION

    print("\nMODEL EVALUATION\n")

    print("MAE =",
          mean_absolute_error(y_test, y_pred))

    print("MSE =",
          mean_squared_error(y_test, y_pred))

    print("RMSE =",
          np.sqrt(mean_squared_error(y_test, y_pred)))

    print("R2 SCORE =",
          r2_score(y_test, y_pred))

    # ACTUAL VS PREDICTED GRAPH

    plt.figure(figsize=(8,6))

    plt.scatter(
        y_test,
        y_pred,
        s=100
    )

    plt.xlabel("Actual Cases")

    plt.ylabel("Predicted Cases")

    plt.title(
        "Actual vs Predicted Cases",
        fontsize=16
    )

    plt.tight_layout()

    plt.show()

    return model
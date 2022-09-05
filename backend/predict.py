from tensorflow import keras
from tensorflow.keras import layers
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import minmax_scale
from pathlib import Path


def build_model():
    starting_data = {
        "lat": [1.4, 4.5, 6.7, 4.5],
        "lon": [3.5, 6.4, 2.4, 6.4],
        "heat": [97.3, 95.3, 85.4, 84.4],
        "rain": [3, 2, 5, 6],
        "day": [4, 5, 6, 7],
        "month": [3, 4, 5, 6],
        "year": [2013, 2019, 2018, 1993],
        # Target tag (fire nearby 20 miles)
        "nearby_fire": [True, True, False, False],
    }

    starting_df = pd.DataFrame(starting_data)

    for col in ["lat", "lon", "heat", "rain", "day", "month", "year"]:
        starting_df[col] = minmax_scale(starting_data[col])

    train, test = train_test_split(starting_df, test_size=0.2, shuffle=True)

    X_df = train.loc[:, starting_df.columns != "nearby_fire"]
    y_df = train[["nearby_fire"]]

    model = keras.Sequential(
        [
            layers.Dense(7, activation="relu", input_dim=7),
            layers.Dense(32, activation="relu"),
            layers.Dense(32, activation="relu"),
            layers.Dense(1),
        ]
    )

    model.compile(optimizer='rmsprop', loss='categorical_crossentropy')
    model.fit(X_df, y_df, epochs=1500, verbose=True)

    model.save("./model")


if not Path("./model").exists():
    build_model()


model = keras.models.load_model("./model")


def predict(pred_data):
    df = pd.DataFrame(
        {
            "lat": pred_data.lat,
            "lon": pred_data.lon,
            "year": pred_data.single_time.year,
            "day": pred_data.single_time.day,
            "month": pred_data.single_time.month,
        }
    )
    return model.predict(df)

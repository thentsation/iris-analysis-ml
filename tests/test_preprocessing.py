import pandas as pd

from preprocessing import preprocess_data

DATA = pd.DataFrame(
    {
        "SepalLengthCm": [5.1, 4.9, 6.3, 6.5],
        "SepalWidthCm": [3.5, 3.0, 3.3, 2.8],
        "Species": ["Setosa", "Setosa", "Versicolor", "Versicolor"],
    }
)


def test_preprocess_data_scales_features_and_keeps_target() -> None:
    X, y = preprocess_data(DATA)

    assert list(X.columns) == ["SepalLengthCm", "SepalWidthCm"]
    assert abs(X["SepalLengthCm"].mean()) < 1e-6
    assert list(y) == ["Setosa", "Setosa", "Versicolor", "Versicolor"]

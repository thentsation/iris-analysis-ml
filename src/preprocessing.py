import pandas as pd
from sklearn.preprocessing import StandardScaler


def preprocess_data(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    X = data.drop(columns=["Species"])
    y = data["Species"]

    X_scaled = StandardScaler().fit_transform(X)
    return pd.DataFrame(X_scaled, columns=X.columns, index=X.index), y

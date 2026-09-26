import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    if data.empty:
        raise ValueError(f"{path} contains no rows")
    return data

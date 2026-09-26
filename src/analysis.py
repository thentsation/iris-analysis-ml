import pandas as pd
import seaborn as sns
from matplotlib.figure import Figure

NUMERIC_COLUMNS = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]


def descriptive_analysis(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    desc_stats = data.describe()
    class_distribution = data["Species"].value_counts()
    return desc_stats, class_distribution


def correlation_matrix(data: pd.DataFrame) -> pd.DataFrame:
    return data[NUMERIC_COLUMNS].corr()


def plot_boxplots(data: pd.DataFrame) -> Figure:
    fig = Figure(figsize=(12, 6))
    ax1, ax2 = fig.subplots(1, 2)
    sns.boxplot(x="Species", y="SepalLengthCm", data=data, ax=ax1)
    ax1.set_title("Distribution of SepalLengthCm by Species")
    sns.boxplot(x="Species", y="PetalWidthCm", data=data, ax=ax2)
    ax2.set_title("Distribution of PetalWidthCm by Species")
    return fig


def plot_petal_scatter(data: pd.DataFrame) -> Figure:
    fig = Figure(figsize=(8, 6))
    ax = fig.subplots()
    sns.scatterplot(
        data=data, x="PetalLengthCm", y="PetalWidthCm", hue="Species", ax=ax
    )
    ax.set_title("Relationship between Petal Length and Width by Species")
    return fig

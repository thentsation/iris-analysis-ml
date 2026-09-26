import pandas as pd
from matplotlib.figure import Figure

from analysis import (
    correlation_matrix,
    descriptive_analysis,
    plot_boxplots,
    plot_petal_scatter,
)

DATA = pd.DataFrame(
    {
        "SepalLengthCm": [5.1, 4.9, 6.3, 6.5],
        "SepalWidthCm": [3.5, 3.0, 3.3, 2.8],
        "PetalLengthCm": [1.4, 1.4, 4.7, 4.6],
        "PetalWidthCm": [0.2, 0.2, 1.6, 1.5],
        "Species": ["Setosa", "Setosa", "Versicolor", "Versicolor"],
    }
)


def test_descriptive_analysis_returns_stats_and_distribution() -> None:
    desc_stats, class_distribution = descriptive_analysis(DATA)

    assert "SepalLengthCm" in desc_stats.columns
    assert class_distribution.to_dict() == {"Setosa": 2, "Versicolor": 2}


def test_correlation_matrix_is_square_and_symmetric() -> None:
    corr = correlation_matrix(DATA)
    assert corr.shape == (4, 4)
    assert (corr.T.round(6) == corr.round(6)).all().all()


def test_plot_boxplots_returns_figure() -> None:
    assert isinstance(plot_boxplots(DATA), Figure)


def test_plot_petal_scatter_returns_figure() -> None:
    assert isinstance(plot_petal_scatter(DATA), Figure)

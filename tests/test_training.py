import pandas as pd
from sklearn.datasets import load_iris

from training import train_and_evaluate_models


def test_train_and_evaluate_models_covers_all_models_with_good_accuracy() -> None:
    iris = load_iris(as_frame=True)
    X = iris.data
    y = pd.Series(iris.target_names[iris.target])

    results = train_and_evaluate_models(X, y)

    assert set(results.keys()) == {"Random Forest", "SVM", "KNN"}
    for result in results.values():
        assert result["accuracy"] > 0.8
        assert "precision" in result["report"]
        assert result["confusion_matrix"].shape == (3, 3)

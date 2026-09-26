from typing import Any

import pandas as pd
from sklearn.base import ClassifierMixin
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

ModelResults = dict[str, dict[str, Any]]


def build_models() -> dict[str, ClassifierMixin]:
    return {
        "Random Forest": RandomForestClassifier(random_state=42),
        "SVM": SVC(),
        "KNN": KNeighborsClassifier(),
    }


def train_and_evaluate_models(
    X: pd.DataFrame, y: pd.Series, test_size: float = 0.3
) -> ModelResults:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )

    results: ModelResults = {}
    for name, model in build_models().items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        results[name] = {
            "accuracy": accuracy_score(y_test, y_pred),
            "report": classification_report(y_test, y_pred),
            "confusion_matrix": confusion_matrix(y_test, y_pred),
        }

    return results

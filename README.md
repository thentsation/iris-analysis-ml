# Iris Dataset Analysis

[![Python CI](https://github.com/thentsation/iris-analysis-ml/actions/workflows/pipeline_python.yaml/badge.svg)](https://github.com/thentsation/iris-analysis-ml/actions/workflows/pipeline_python.yaml)
[![Docker CI/CD](https://github.com/thentsation/iris-analysis-ml/actions/workflows/pipeline_docker.yaml/badge.svg)](https://github.com/thentsation/iris-analysis-ml/actions/workflows/pipeline_docker.yaml)

> Leia em [português](README.pt-br.md).

Exploratory data analysis and classification (Random Forest, SVM, KNN) on the Iris dataset. The original exploration lives in [`notebooks/irisML.ipynb`](notebooks/irisML.ipynb); the same logic is also extracted into a tested `src/` package.

An in-depth write-up of the productization of this project is available in [ARTIGO.md](ARTIGO.md) (pt-br) / [ARTIGO.en-us.md](ARTIGO.en-us.md) (en-us).

## Project structure

```text
src/
├── data_loader.py     # load_data(path)
├── analysis.py         # descriptive stats, correlation matrix, boxplot/scatter figures
├── preprocessing.py    # feature scaling
├── training.py          # Random Forest / SVM / KNN, returns accuracy + report + confusion matrix
└── main.py               # runs the whole pipeline and prints the results
notebooks/irisML.ipynb    # the original exploratory notebook
```

## Getting started

```bash
make install    # creates .venv and installs deps
make run        # runs the full analysis + training pipeline against data/iris.csv
make notebook   # opens the original exploratory notebook
```

Run with Docker instead:

```bash
make docker-build
make docker-run
```

## Development

```bash
make test        # pytest
make coverage     # pytest with coverage report
make lint         # ruff check
make format       # ruff format
make typecheck    # mypy
```

CI runs ruff, pytest (coverage gate), mypy and pip-audit on every push/PR, plus a scheduled daily run. Docker images are built, scanned with Trivy, and published to GHCR on `main`. Dependabot keeps pip, the Docker base image, and GitHub Actions up to date, with patch/minor bumps auto-merged. Releases are tagged automatically with [python-semantic-release](https://python-semantic-release.readthedocs.io/).

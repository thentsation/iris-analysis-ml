# Iris Dataset Analysis

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

CI and deploy run on the platform's Jenkins (`Jenkinsfile` → `appPipeline` from the `platform` Shared Library, repo devops-platform), triggered by webhooks; there are no GitHub Actions.

- **PRs and branches** — contract validation; `docker build --target test` (`ruff check`, `ruff format --check`, `mypy`, `pytest` with ≥90% coverage on Python 3.11 and 3.12, tool versions from `config/requirements-dev.txt`); `pip-audit` on `config/requirements.lock`; Trivy (CRITICAL/HIGH) on the runtime image.
- **main** — all of the above, then build and a test run of the image (the job must exit 0; nothing stays running), release with python-semantic-release (version, CHANGELOG, tag and GitHub release) and a rebuild of the portfolio. Also rebuilt every Monday to pick up security patches.
- **Dependencies** — Renovate (Jenkins job `platform/renovate`, `renovate.json` → devops-platform preset): daily updates, weekly lockfile maintenance, Dependency Dashboard issue and auto-merge of patch/minor after Jenkins passes.

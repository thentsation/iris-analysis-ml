# Iris Dataset Analysis

[![Python CI](https://github.com/thentsation/iris-analysis-ml/actions/workflows/pipeline_python.yaml/badge.svg)](https://github.com/thentsation/iris-analysis-ml/actions/workflows/pipeline_python.yaml)
[![Docker CI/CD](https://github.com/thentsation/iris-analysis-ml/actions/workflows/pipeline_docker.yaml/badge.svg)](https://github.com/thentsation/iris-analysis-ml/actions/workflows/pipeline_docker.yaml)

> Read in [English](README.md).

Análise exploratória e classificação (Random Forest, SVM, KNN) no dataset Iris. A exploração original vive em [`notebooks/irisML.ipynb`](notebooks/irisML.ipynb); a mesma lógica também foi extraída para um pacote `src/` testado.

Um artigo detalhado sobre a produtização deste projeto está disponível em [ARTIGO.md](ARTIGO.md) (pt-br) / [ARTIGO.en-us.md](ARTIGO.en-us.md) (en-us).

## Estrutura do projeto

```text
src/
├── data_loader.py     # load_data(path)
├── analysis.py         # estatísticas descritivas, matriz de correlação, figuras de boxplot/scatter
├── preprocessing.py    # normalização das features
├── training.py          # Random Forest / SVM / KNN, retorna acurácia + relatório + matriz de confusão
└── main.py               # roda o pipeline inteiro e imprime os resultados
notebooks/irisML.ipynb    # o notebook exploratório original
```

## Como rodar

```bash
make install    # cria o .venv e instala as deps
make run        # roda a análise + treino completos contra data/iris.csv
make notebook   # abre o notebook exploratório original
```

Rodando com Docker:

```bash
make docker-build
make docker-run
```

## Desenvolvimento

```bash
make test        # pytest
make coverage     # pytest com relatório de cobertura
make lint         # ruff check
make format       # ruff format
make typecheck    # mypy
```

O CI roda ruff, pytest (com piso de cobertura), mypy e pip-audit em todo push/PR, além de uma execução diária agendada. Imagens Docker são construídas, escaneadas com Trivy e publicadas no GHCR na `main`. O Dependabot mantém pip, imagem base do Docker e GitHub Actions atualizados, com bumps patch/minor mesclados automaticamente. Releases são versionados automaticamente com [python-semantic-release](https://python-semantic-release.readthedocs.io/).

# Iris Dataset Analysis

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

CI e deploy rodam no Jenkins da plataforma (`Jenkinsfile` → `appPipeline` da Shared Library `platform`, repo devops-platform), disparados por webhooks. Sem GitHub Actions.

- **PRs e branches** — validação do contrato; `docker build --target test` (`ruff check`, `ruff format --check`, `mypy`, `pytest` com cobertura ≥90% em Python 3.11 e 3.12, versões das ferramentas no `config/requirements-dev.txt`); `pip-audit` no `config/requirements.lock`; Trivy (CRITICAL/HIGH) na imagem de runtime.
- **main** — tudo acima e depois build e uma execução de teste da imagem (o job precisa terminar com exit 0; nada fica no ar), release com o python-semantic-release (versão, CHANGELOG, tag e release no GitHub) e rebuild do portfolio. Também é reconstruída toda segunda para pegar patches de segurança.
- **Dependências** — Renovate (job `platform/renovate` no Jenkins, `renovate.json` → preset do devops-platform): atualizações diárias, manutenção semanal do lockfile, issue "Dependency Dashboard" e auto-merge de patch/minor depois que o Jenkins aprova.

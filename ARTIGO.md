🇧🇷 Português | [🇺🇸 English](ARTIGO.en-us.md)

# Um notebook onde as funções recebiam um parâmetro e usavam outra coisa

Esse era um notebook de EDA clássico — describe(), boxplots, correlação, três classificadores. Fazia o que prometia. O bug estava escondido num padrão que se repetia em quase toda função:

```python
def descriptive_analysis(date):
    desc_stats = data.describe()
    ...

def preprocess_data(date):
    X = data.drop(columns=['Species'])
    ...
```

Repare no parâmetro: `date` (não `data` — typo), e ele **nunca é usado**. Toda função lia a variável global `data` do notebook, ignorando o argumento recebido. Funcionava porque, num notebook, rodar as células em ordem sempre deixa `data` no escopo global certo — mas isso significa que as funções não são reutilizáveis fora do notebook, e teriam se comportado de forma sutilmente errada no primeiro momento em que alguém chamasse `descriptive_analysis(outro_dataframe)` esperando que funcionasse com `outro_dataframe`.

## Extraindo pra fora do escopo global

Todo esse conjunto de funções virou um pacote `src/` de verdade, onde cada função usa o parâmetro que recebe (óbvio, mas era exatamente o que faltava):

```python
def descriptive_analysis(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    desc_stats = data.describe()
    class_distribution = data["Species"].value_counts()
    return desc_stats, class_distribution
```

Isso também resolveu outro problema do original: as funções só imprimiam (`print(...)`), nunca retornavam nada, então não tinha como testá-las ou reusar o resultado programaticamente. Agora `descriptive_analysis`, `correlation_matrix` e `train_and_evaluate_models` retornam dados estruturados; quem chama decide o que fazer com eles (imprimir, plotar, servir via API).

## Gráficos que não dependem de um display

As funções de plot originais usavam `plt.figure()` + `plt.show()` — ótimo interativamente, inútil pra testar (e barulhento em CI headless). Troquei por `matplotlib.figure.Figure()` direto, sem depender do estado global do pyplot nem de um backend interativo, retornando a `Figure` pra quem chamou decidir se mostra, salva em disco, ou (no caso dos testes) só verifica que o tipo e o conteúdo estão corretos:

```python
def plot_boxplots(data: pd.DataFrame) -> Figure:
    fig = Figure(figsize=(12, 6))
    ax1, ax2 = fig.subplots(1, 2)
    sns.boxplot(x="Species", y="SepalLengthCm", data=data, ax=ax1)
    ...
    return fig
```

## Determinismo no treino

`RandomForestClassifier()` não tinha `random_state`, então a acurácia mudava (levemente) a cada execução — inofensivo numa demo interativa, mas incompatível com um teste que afirma "a acurácia deve ser maior que 0.8". Adicionei `random_state=42`, consistente com o `train_test_split` que já usava a mesma seed.

## O notebook original continua aqui

Não reescrevi `notebooks/irisML.ipynb` — ele continua sendo a exploração original, com as saídas e a narrativa de quando foi escrito. O pacote `src/` é a versão testada e reutilizável da mesma lógica, não uma substituição do notebook.

## O resto do padrão

CI completo (ruff, pytest com piso de 90%, mypy, pip-audit, Docker+Trivy+GHCR — já com o `skip-dirs` do `pip/_vendor/msgpack` desde o primeiro commit), dependabot com auto-merge, dashboard de dependências, atualização semanal de lockfile, release semântico. O Dockerfile empacota o pipeline como um script batch (`ENTRYPOINT ["python", "src/main.py"]`, sem porta exposta) — é uma análise, não um serviço.

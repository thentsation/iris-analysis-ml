[🇧🇷 Português](ARTIGO.md) | 🇺🇸 English

# A notebook where every function took a parameter and used something else

This was a classic EDA notebook — describe(), boxplots, correlation, three classifiers. It did what it promised. The bug was hiding in a pattern that repeated in almost every function:

```python
def descriptive_analysis(date):
    desc_stats = data.describe()
    ...

def preprocess_data(date):
    X = data.drop(columns=['Species'])
    ...
```

Look at the parameter: `date` (not `data` — a typo), and it's **never used**. Every function read the notebook's global `data` variable, ignoring the argument it received. It worked because, in a notebook, running cells in order always leaves `data` in the right global scope — but it means the functions aren't reusable outside the notebook, and would have behaved subtly wrong the first time anyone called `descriptive_analysis(some_other_dataframe)` expecting it to actually work on `some_other_dataframe`.

## Pulling it out of global scope

The whole set of functions became a real `src/` package, where every function uses the parameter it receives (obvious, but that was exactly what was missing):

```python
def descriptive_analysis(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    desc_stats = data.describe()
    class_distribution = data["Species"].value_counts()
    return desc_stats, class_distribution
```

This also fixed another problem with the original: the functions only printed (`print(...)`), never returned anything, so there was no way to test them or reuse the result programmatically. Now `descriptive_analysis`, `correlation_matrix`, and `train_and_evaluate_models` return structured data; the caller decides what to do with it (print it, plot it, serve it through an API).

## Plots that don't depend on a display

The original plotting functions used `plt.figure()` + `plt.show()` — great interactively, useless for testing (and noisy in headless CI). I swapped these for `matplotlib.figure.Figure()` directly, without depending on pyplot's global state or an interactive backend, returning the `Figure` for the caller to decide whether to show it, save it to disk, or — in the tests' case — just check its type and content:

```python
def plot_boxplots(data: pd.DataFrame) -> Figure:
    fig = Figure(figsize=(12, 6))
    ax1, ax2 = fig.subplots(1, 2)
    sns.boxplot(x="Species", y="SepalLengthCm", data=data, ax=ax1)
    ...
    return fig
```

## Determinism in training

`RandomForestClassifier()` had no `random_state`, so accuracy shifted (slightly) on every run — harmless in an interactive demo, incompatible with a test asserting "accuracy should be above 0.8." I added `random_state=42`, consistent with the `train_test_split` that already used the same seed.

## The original notebook is still here

I didn't rewrite `notebooks/irisML.ipynb` — it remains the original exploration, with the outputs and narrative from when it was written. The `src/` package is the tested, reusable version of the same logic, not a replacement for the notebook.

## The rest of the pattern

Full CI (ruff, pytest with a 90% floor, mypy, pip-audit, Docker+Trivy+GHCR — already with the `pip/_vendor/msgpack` `skip-dirs` from the first commit), dependabot with auto-merge, dependency dashboard, weekly lockfile refresh, semantic release. The Dockerfile packages the pipeline as a batch script (`ENTRYPOINT ["python", "src/main.py"]`, no port exposed) — it's an analysis, not a service.

import main as main_module


def test_main_runs_end_to_end(capsys) -> None:
    main_module.main("data/iris.csv")

    output = capsys.readouterr().out
    assert "Descriptive Statistics" in output
    assert "Model Evaluation Random Forest" in output

import pytest

from data_loader import load_data


def test_load_data_reads_csv(tmp_path) -> None:
    csv_path = tmp_path / "iris.csv"
    csv_path.write_text("SepalLengthCm,Species\n5.1,Setosa\n4.9,Setosa\n")

    df = load_data(str(csv_path))

    assert list(df.columns) == ["SepalLengthCm", "Species"]
    assert len(df) == 2


def test_load_data_raises_on_missing_file() -> None:
    with pytest.raises(FileNotFoundError):
        load_data("does/not/exist.csv")


def test_load_data_raises_on_empty_file(tmp_path) -> None:
    csv_path = tmp_path / "empty.csv"
    csv_path.write_text("SepalLengthCm,Species\n")

    with pytest.raises(ValueError, match="no rows"):
        load_data(str(csv_path))

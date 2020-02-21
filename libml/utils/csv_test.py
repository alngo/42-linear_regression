from .csv import get_parameters
import pytest


def test_get_parameters_with_none(capsys):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        get_parameters(None)
    captured = capsys.readouterr()
    assert captured.out == 'An unexpected error occured on read_csv\n'
    assert pytest_wrapped_e.value.code == 1


def test_get_parameters_with_empty_file(capsys):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        path = "./models/empty.csv"
        get_parameters(path)
    captured = capsys.readouterr()
    assert captured.out == 'File at path: "./models/empty.csv" not found\n'
    assert pytest_wrapped_e.value.code == 1


def test_get_parameters_with_invalid_path(capsys):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        path = "./models/qwe.csv"
        get_parameters(path)
    captured = capsys.readouterr()
    assert captured.out == 'File at path: "./models/qwe.csv" not found\n'
    assert pytest_wrapped_e.value.code == 1


def test_get_parameters_with_valid_path(capsys):
    path = "./models/test.csv"
    parameters = get_parameters(path)
    captured = capsys.readouterr()
    assert parameters[0] == "42"
    assert parameters[1] == "24"

from .reader import Reader


def test_reader_init():
    path = "./models/test.csv"
    r = Reader(1, path=path)
    assert r.args[0] == 1
    assert r.path == path
    assert r.parameters[0] == "42"
    assert r.parameters[1] == "24"


def test_reader_linear_regression():
    r = Reader(1, path="./models/test.csv")
    predicted = r.linear_regression()
    assert predicted == 66

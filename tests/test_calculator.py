from src.calculator import add, substract


def test_add():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(0, 0) == 0


def test_substract():
    assert substract(5, 3) == 2
    assert substract(-1, -1) == 0
    assert substract(0, 5) == -5

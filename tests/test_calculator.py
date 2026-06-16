from src.calculator import add, substract, multiply, divide


def test_add():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(0, 0) == 0


def test_substract():
    assert substract(5, 3) == 2
    assert substract(-1, -1) == 0
    assert substract(0, 5) == -5


def test_multiply():

    assert multiply(2, 3) == 6
    assert multiply(-1, -1) == 1
    assert multiply(0, 5) == 0


def test_divide():

    assert divide(6, 3) == 2
    assert divide(-1, -1) == 1


def test_divide_by_zero():
    try:
        divide(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."
    else:
        assert False, "Expected ValueError when dividing by zero."

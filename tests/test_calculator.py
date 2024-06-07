import pytest
from utilities.calculator import Calculator


@pytest.mark.parametrize('a, b, result', [
    (1, 2, 3),
    (2, -3, -1),
    (-3, -7, -10),
    (9, 0, 9)
])
def test_sum(a, b, result):
    assert Calculator.sum(a, b) == result


@pytest.mark.parametrize('a, b, result', [
    (1, 2, -1),
    (2, -3, 5),
    (-3, -7, 4),
    (9, 0, 9)
])
def test_sub(a, b, result):
    assert Calculator.sub(a, b) == result


@pytest.mark.parametrize('a, b, result', [
    (1, 2, 2),
    (2, -3, -6),
    (-3, -7, 21),
    (9, 0, 0)
])
def test_mul(a, b, result):
    assert Calculator.mul(a, b) == result


@pytest.mark.parametrize('a, b, result', [
    (1, 2, 0.5),
    (2, 1, 2),
    (7, 0, 'Не определено'),
    (0, 4, 0)
])
def test_div(a, b, result):
    assert Calculator.div(a, b) == result


@pytest.mark.parametrize('a, b, result', [
    (1, 2, 0),
    (5, 2, 2),
    (7, 0, 'Не определено'),
    (0, 4, 0),
    (6, 3, 2),
    (11, 6, 1)
])
def test_int_div(a, b, result):
    assert Calculator.int_div(a, b) == result


@pytest.mark.parametrize('a, b, result', [
    (1, 2, 1),
    (15, 5, 0),
    (7, 0, 'Не определено'),
    (13, 10, 3),
    (21, 5, 1)
])
def test_rem(a, b, result):
    assert Calculator.rem(a, b) == result

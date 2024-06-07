import pytest
from calculator import Calculator


@pytest.mark.parametrize('a, b, result', [
    (1, 2, 3),
    (2, -3, -1),
    (-3, -7, -10),
    (9, 0, 9)
])
def sum_test(a, b, result):
    assert Calculator.sum(a, b) == result


@pytest.mark.parametrize('a, b, result', [
    (1, 2, -1),
    (2, -3, 5),
    (-3, -7, 4),
    (9, 0, 9)
])
def sub_test(a, b, result):
    assert Calculator.sub(a, b) == result

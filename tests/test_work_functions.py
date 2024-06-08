import pytest
from utilities.work_functions import greeting, sort_array, find_element


def test_greeting():
    assert greeting('Ivan') == 'Hello, Ivan'


@pytest.mark.parametrize('arr, result', [
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([7, 2, 1, 8, 4], [1, 2, 4, 7, 8]),
    ([1], [1]),
    ([], [])
])
def test_sort_array(arr, result):
    assert sort_array(arr) == result


@pytest.mark.parametrize('arr, target, result', [
    ([6, 2, 1, 7, 4], 7, 3),
    ([3, 5, 5, 1, 5], 5, 1),
    ([1, 2, 3, 4, 5], 8, -1)
])
def test_find_element(arr, target, result):
    assert find_element(arr, target) == result

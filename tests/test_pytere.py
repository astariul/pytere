import pytest

from pytere import is_odd


@pytest.mark.parametrize("x", [1, 3, 7, 348973243, -1])
def test_with_odd_numbers(x):
    assert is_odd(x)


@pytest.mark.parametrize("x", [0, 2, 10, 74353434, -8])
def test_with_even_numbers(x):
    assert not is_odd(x)

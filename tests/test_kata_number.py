import pytest
from code_pathshala.labs.kata_numbers import factorial


def test_factorial_zero_and_one():
    assert factorial(0) == 1
    assert factorial(1) == 1


def test_factorial_positive_integers():
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(10) == 3628800


def test_factorial_negative_value():
    with pytest.raises(ValueError, match="n must be >= 0"):
        factorial(-1)
    with pytest.raises(ValueError, match="n must be >= 0"):
        factorial(-10)

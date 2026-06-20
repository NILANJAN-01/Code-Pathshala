import pytest
from code_pathshala.utils import math_ops


def test_add():
    assert math_ops.add(2, 3) == 5
    assert math_ops.add(-1, 1) == 0
    assert math_ops.add(0, 0) == 0
    assert math_ops.add(2.5, 3.5) == 6.0


def test_subtract():
    assert math_ops.subtract(5, 3) == 2
    assert math_ops.subtract(0, 10) == -10
    assert math_ops.subtract(-5, -5) == 0


def test_multiply():
    assert math_ops.multiply(3, 4) == 12
    assert math_ops.multiply(-2, 5) == -10
    assert math_ops.multiply(0, 100) == 0


def test_divide():
    assert math_ops.divide(10, 2) == 5.0
    assert math_ops.divide(5, 2) == 2.5
    assert math_ops.divide(-6, 3) == -2.0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        math_ops.divide(10, 0)


def test_mean():
    assert math_ops.mean([1, 2, 3, 4, 5]) == 3.0
    assert math_ops.mean([10.0, 20.0]) == 15.0
    assert math_ops.mean([7]) == 7.0


def test_mean_empty_list():
    with pytest.raises(ValueError, match="List cannot be empty"):
        math_ops.mean([])

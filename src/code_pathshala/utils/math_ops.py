"""
Reusable math utilities.
"""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference between two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def mean(values: list[float]) -> float:
    """Return the average of a list of values."""
    if not values:
        raise ValueError("List cannot be empty")
    return sum(values) / len(values)

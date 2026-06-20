"""
Number practice (Katas) – loops and logic.
"""


def factorial(n: int) -> int:
    """Compute factorial using loops."""
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

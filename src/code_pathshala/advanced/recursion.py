"""
Recursion Module.
Illustrates base cases, recursive calls, call stack buildup, and optimization via memoization.
"""


def fibonacci(n: int) -> int:
    """
    Standard recursive Fibonacci sequence calculator.
    Traces recursive branching calls (accumulates call stack frames).
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Dictionary cache for memoization
_memo_cache: dict[int, int] = {}


def fibonacci_memo(n: int) -> int:
    """
    Optimized Fibonacci using memoization.
    Avoids re-evaluating sub-branches by caching results in memory.
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n in _memo_cache:
        return _memo_cache[n]

    result = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    _memo_cache[n] = result
    return result

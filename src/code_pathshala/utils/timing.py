"""
Tiny timing decorator – measure how long a function takes to run.
"""

import time
from typing import Callable, TypeVar

F = TypeVar("F", bound=Callable[..., object])


def timed(func: F) -> F:  # type: ignore[override]
    def wrapper(*args, **kwargs):  # type: ignore[no-redef]
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            end = time.perf_counter()
            duration = (end - start) * 1000
            print(f"{func.__name__} took {duration:.2f} ms")

    return wrapper  # type: ignore[return-value]

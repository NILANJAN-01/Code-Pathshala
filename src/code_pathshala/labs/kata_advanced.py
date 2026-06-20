"""
Advanced Python Lab Challenge (Kata).
Implement a decorator to track call counts and a generator yielding prime numbers.
"""

from typing import Any, Callable, Generator, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def count_calls(func: F) -> F:
    """
    A decorator that counts how many times a function is executed.
    Store the count in a 'calls' attribute on the wrapper function.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper  # type: ignore[return-value]


def is_prime(num: int) -> bool:
    """Helper function to check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_generator(limit: int) -> Generator[int, None, None]:
    """
    A generator function that yields prime numbers up to a specified limit.
    """
    for n in range(2, limit + 1):
        if is_prime(n):
            yield n

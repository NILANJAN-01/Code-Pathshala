"""
Decorators and Closures Module.
Illustrates function wrapping, closures, and meta-programming using decorator syntax.
"""

from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def log_call(func: F) -> F:
    """
    A decorator that logs when a function starts, its arguments, and its return value.
    Demonstrates closure capturing of the inner wrapped function scope.
    """
    # Use lists to accumulate logs dynamically for testing/validation
    log_call.logs = getattr(log_call, "logs", [])  # type: ignore

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        args_str = ", ".join(repr(a) for a in args)
        log_call.logs.append(f"Calling {func.__name__}({args_str})")  # type: ignore
        result = func(*args, **kwargs)
        log_call.logs.append(f"{func.__name__} returned {repr(result)}")  # type: ignore
        return result

    return wrapper  # type: ignore[return-value]


@log_call
def greet_user(username: str) -> str:
    """Demo function wrapped by log_call decorator."""
    return f"Welcome back, {username}!"

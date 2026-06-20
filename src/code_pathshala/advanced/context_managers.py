"""
Context Managers Module.
Demonstrates clean resource handling (opening/closing/safety locks) using the 'with' statement.
"""

from typing import Any


class ResourceLock:
    """
    A custom context manager simulating acquiring and releasing a thread/database lock.
    """

    def __init__(self, resource_name: str):
        self.resource_name = resource_name
        self.is_locked = False
        self.log_history: list[str] = []

    def __enter__(self) -> "ResourceLock":
        """Acquires lock when entering the 'with' scope."""
        self.is_locked = True
        self.log_history.append(f"Lock acquired on: {self.resource_name}")
        return self

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> bool:
        """Releases lock when exiting the 'with' scope, even if exceptions are raised."""
        self.is_locked = False
        self.log_history.append(f"Lock released on: {self.resource_name}")

        # Log exception handling if an error occurred inside the scope
        if exc_type is not None:
            self.log_history.append(f"Handled error: {exc_value}")
            # Returning True suppresses the exception, returning False propagates it.
            # For education, we propagate the error but log that we safely closed the resource.
            return False
        return True

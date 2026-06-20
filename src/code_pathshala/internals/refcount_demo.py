"""
Reference Counting Demonstration Module.
Shows how Python tracks allocations using reference counting in the heap.
"""

import sys
from typing import Any


def get_actual_refcount(obj: Any) -> int:
    """
    Returns the true reference count of an object.
    We subtract 1 because passing the object to getrefcount() creates a temporary reference.
    """
    return sys.getrefcount(obj) - 1


def trace_reference_counts() -> list[int]:
    """
    Traces reference count changes through variable assignments and deletes.
    Returns:
        List of reference counts at different steps.
    """
    ref_history = []

    # Create a unique object (e.g. custom list, avoiding integer/string caching)
    x = ["unique_mem_element_1234"]
    ref_history.append(get_actual_refcount(x))  # 1 reference (x)

    # Alias assignment
    y = x
    ref_history.append(get_actual_refcount(x))  # 2 references (x, y)

    # Another alias
    z = y
    ref_history.append(get_actual_refcount(x))  # 3 references (x, y, z)

    # Delete one alias
    del z
    ref_history.append(get_actual_refcount(x))  # 2 references (x, y)

    # Delete another alias
    del y
    ref_history.append(get_actual_refcount(x))  # 1 reference (x)

    return ref_history

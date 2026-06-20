"""
Mutability and Memory Layout Module.
Demonstrates object identity, variable aliasing, mutability vs immutability, and copy behaviors.
"""

import copy
from typing import Any


def check_identity(a: Any, b: Any) -> bool:
    """Check if two variables point to the exact same object in RAM (same memory ID)."""
    return id(a) == id(b)


def demonstrate_aliasing() -> tuple[list[int], list[int], bool]:
    """
    Shows how assignment creates an alias (pointing to the same object).
    Modifying the alias changes the original.
    """
    original = [1, 2, 3]
    alias = original
    alias.append(4)
    # Check identity
    is_same = check_identity(original, alias)
    return original, alias, is_same


def demonstrate_shallow_copy() -> tuple[list[list[int]], list[list[int]], bool, bool]:
    """
    Shows how copy() creates a new outer list but copies references of inner objects (shallow).
    Modifying nested structures affects both list copies.
    """
    original = [[1, 2], [3, 4]]
    shallow = original.copy()

    # Outers are different objects
    outer_same = check_identity(original, shallow)

    # Inners are the SAME objects
    inner_same_before = check_identity(original[0], shallow[0])

    # Modifying a nested list
    shallow[0].append(99)

    return original, shallow, outer_same, inner_same_before


def demonstrate_deep_copy() -> tuple[list[list[int]], list[list[int]], bool, bool]:
    """
    Shows how deepcopy() duplicates both the outer lists and all nested structures.
    Modifying the copy has no effect on the original.
    """
    original = [[1, 2], [3, 4]]
    deep = copy.deepcopy(original)

    # Outers are different
    outer_same = check_identity(original, deep)

    # Inners are also different
    inner_same_before = check_identity(original[0], deep[0])

    # Modifying a nested list
    deep[0].append(99)

    return original, deep, outer_same, inner_same_before

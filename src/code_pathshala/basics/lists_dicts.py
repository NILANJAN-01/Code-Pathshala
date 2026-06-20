"""
List and dictionary examples.
"""


def unique_sorted(items: list[int]) -> list[int]:
    """Return a sorted list of unique elements."""
    return sorted(set(items))


def invert(d: dict[str, int]) -> dict[int, str]:
    """Swap keys and values of a dictionary."""
    return {v: k for k, v in d.items()}

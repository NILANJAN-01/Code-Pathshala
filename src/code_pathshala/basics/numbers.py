"""
Simple numeric operations for beginners.
"""

def square(num: float) -> float:
    """Return the square of a number."""
    return num ** 2

def cube(num: float) -> float:
    """Return the cube of a number."""
    return num ** 3

def average(nums: list[float]) -> float:
    """Return the average of a list of numbers."""
    if not nums:
        raise ValueError("List cannot be empty")
    return sum(nums) / len(nums)

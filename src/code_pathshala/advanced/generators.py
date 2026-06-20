"""
Generators and Iterators Module.
Demonstrates memory-efficient streaming of values using yield and generator expressions.
"""

from typing import Generator


def count_up_to(max_val: int) -> Generator[int, None, None]:
    """
    Generator function that yields integers from 1 up to max_val.
    Illustrates how code execution is suspended between yield statements, keeping memory low.
    """
    count = 1
    while count <= max_val:
        yield count
        count += 1


def get_squares_generator(numbers: list[int]) -> Generator[int, None, None]:
    """
    Returns square values of a list of numbers.
    Demonstrates lazy evaluation on collection sequences.
    """
    for num in numbers:
        yield num * num

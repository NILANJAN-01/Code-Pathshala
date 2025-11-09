"""
Loops and conditions – examples using if/else and for loops.
"""

def fizzbuzz(n: int) -> list[str]:
    """
    Classic FizzBuzz problem.
    Returns a list of strings from 1..n with:
        "Fizz" for multiples of 3,
        "Buzz" for multiples of 5,
        "FizzBuzz" for multiples of both.
    """
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

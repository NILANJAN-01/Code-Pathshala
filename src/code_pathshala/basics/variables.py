"""
Variables 101 – learn how to store and use data.
"""

def make_profile(name: str, age: int) -> dict:
    """
    Create a small profile dictionary.
    Example:
        >>> make_profile("Nilanjan", 25)
        {'name': 'Nilanjan', 'age': 25}
    """
    return {"name": name, "age": age}

"""
String basics – functions for text manipulation.
"""

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

def shout(text: str) -> str:
    """Return the text in uppercase."""
    return text.upper()

def title_case(text: str) -> str:
    """Return the text in title case (capitalize each word)."""
    return text.title()

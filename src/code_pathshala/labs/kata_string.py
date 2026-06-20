"""
String practice (Katas) – for students to improve logic.
"""


def reverse_words(text: str) -> str:
    """Return the sentence with words reversed."""
    return " ".join(reversed(text.split()))


def is_palindrome(text: str) -> bool:
    """Check if text is palindrome (ignoring case and punctuation)."""
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

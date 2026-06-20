from code_pathshala.labs.kata_string import reverse_words, is_palindrome


def test_reverse_words():
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("Python is fun") == "fun is Python"
    assert reverse_words("  multiple   spaces  here  ") == "here spaces multiple"
    assert reverse_words("") == ""
    assert reverse_words("single") == "single"


def test_is_palindrome():
    # Simple palindromes
    assert is_palindrome("radar") is True
    assert is_palindrome("Racecar") is True  # Ignore case
    assert (
        is_palindrome("A man, a plan, a canal: Panama") is True
    )  # Ignore punctuation/spaces

    # Non-palindromes
    assert is_palindrome("hello") is False
    assert is_palindrome("python") is False

    # Edge cases
    assert is_palindrome("") is True
    assert is_palindrome("a") is True

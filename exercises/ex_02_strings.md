# Lesson 2: String Manipulation in Python

Welcome to Lesson 2! In this exercise, we will learn about **Strings** in Python, how they are indexed and sliced, and how to use built-in string methods to manipulate text.

---

## 1. Creating Strings
In Python, strings are sequences of character data. They are created by enclosing characters in quotes:

```python
single_quote_str = 'Hello'
double_quote_str = "World"
multiline_str = """This is a
multiline string in Python."""
```

---

## 2. String Indexing and Slicing
Because strings are sequences, each character in a string has an index starting from `0`.

```
 String:  P   y   t   h   o   n
  Index:  0   1   2   3   4   5
Neg Idx: -6  -5  -4  -3  -2  -1
```

### Examples
* **Indexing:** Access a single character.
  ```python
  s = "Python"
  print(s[0])   # Output: 'P'
  print(s[-1])  # Output: 'n' (last character)
  ```
* **Slicing:** Access a substring using the syntax `[start:stop:step]`. Note that the `stop` index is *exclusive*.
  ```python
  print(s[0:2])  # Output: 'Py'
  print(s[2:])   # Output: 'thon'
  print(s[::-1]) # Output: 'nohtyP' (reverses string)
  ```

---

## 3. String Methods
Python provides many built-in methods to manipulate strings. Strings in Python are **immutable**, meaning methods return a *new* string rather than modifying the original.

* `.upper()` / `.lower()`: Change case.
* `.strip()`: Remove leading/trailing whitespace.
* `.replace(old, new)`: Replace occurrences of a substring.
* `.split(delimiter)`: Split a string into a list of substrings.
* `delimiter.join(list)`: Combine a list of strings into one string.

```python
text = "  hello world  "
print(text.strip().title())  # Output: "Hello World"
```

---

## 4. String Formatting (f-strings)
F-strings provide a concise, readable way to format strings by embedding Python expressions directly inside string literals:

```python
name = "Alice"
score = 98.5
message = f"Congratulations {name}, your score is {score}%!"
print(message)  # Output: Congratulations Alice, your score is 98.5%!
```

---

## 5. Hands-on Practice
Explore these files to see string operations in action:
* [strings.py](file:///C:/Users/smpni/.gemini/antigravity/scratch/Code-Pathshala/src/code_pathshala/basics/strings.py): Basic operations like greeting and casing.
* [kata_string.py](file:///C:/Users/smpni/.gemini/antigravity/scratch/Code-Pathshala/src/code_pathshala/labs/kata_string.py): Advanced string challenges (e.g. palindromes and word reversal).

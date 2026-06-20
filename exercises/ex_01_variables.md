# Lesson 1: Variables & Data Types in Python

Welcome to your first Python lesson! In this exercise, we will learn about **variables**, **data types**, and how to store/manipulate information in Python.

---

## 1. What is a Variable?
In programming, a **variable** is a named location in the computer's memory used to store data. Think of it as a labeled storage box.

In Python, you create a variable by assigning it a value using the assignment operator (`=`):

```python
name = "Alice"
age = 25
is_student = True
```

---

## 2. Basic Data Types
Python automatically detects the type of value you assign to a variable (this is called *dynamic typing*). The most common primitive data types are:

| Data Type | Description | Example |
|---|---|---|
| **String (`str`)** | Text wrapped in single or double quotes | `"Hello"`, `'Python'` |
| **Integer (`int`)** | Whole numbers without decimals | `10`, `-5`, `0` |
| **Float (`float`)** | Decimal or real numbers | `3.14`, `-0.01` |
| **Boolean (`bool`)**| Logical values (must be capitalized) | `True`, `False` |

### Checking Data Types
You can check the type of any variable using the built-in `type()` function:
```python
x = 10.5
print(type(x))  # Output: <class 'float'>
```

---

## 3. Variable Naming Rules
When naming variables in Python, you must follow these conventions:
* Must start with a letter or an underscore (`_`).
* Cannot start with a number.
* Can only contain alphanumeric characters and underscores (`A-z`, `0-9`, and `_`).
* Are case-sensitive (`age`, `Age`, and `AGE` are three different variables).
* Cannot be Python keywords (like `if`, `while`, `import`, etc.).
* **Best Practice:** Use **snake_case** for multi-word variable names (e.g., `user_profile_name`).

---

## 4. Hands-on Practice
Open the file [variables.py](file:///C:/Users/smpni/.gemini/antigravity/scratch/Code-Pathshala/src/code_pathshala/basics/variables.py) to see how simple functions return dictionary objects constructed from variables. 

Try running python interactively and experimenting:
```python
from code_pathshala.basics.variables import make_profile
profile = make_profile("Nilanjan", 25)
print(profile) # {'name': 'Nilanjan', 'age': 25}
```

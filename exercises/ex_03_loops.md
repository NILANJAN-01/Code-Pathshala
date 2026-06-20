# Lesson 3: Control Flow and Loops in Python

Welcome to Lesson 3! In this exercise, we will master **control flow**: making decisions with conditional statements and repeating tasks with loops.

---

## 1. Conditionals (`if`, `elif`, `else`)
Conditional statements run different blocks of code depending on whether a boolean expression evaluates to `True` or `False`.

Python uses indentation to define the scope of blocks:

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")
```

### Logical Operators
Combine multiple conditions using:
* `and`: True if *both* conditions are True.
* `or`: True if *at least one* condition is True.
* `not`: Inverts the boolean value.

---

## 2. While Loops
A `while` loop executes a block of code as long as a specified condition remains `True`.

```python
count = 1
while count <= 5:
    print(f"Count is {count}")
    count += 1
```

> [!WARNING]
> Always ensure the loop condition eventually becomes `False`, otherwise you will create an **infinite loop**!

---

## 3. For Loops
`for` loops are used to iterate over a sequence (such as a list, tuple, dictionary, set, or string).

### Iterating through a Range
The `range()` function generates a sequence of numbers. Syntax: `range(start, stop, step)`. Note: `stop` is exclusive.

```python
# Iterates from 0 up to 4 (5 is excluded)
for i in range(5):
    print(i)
```

### Iterating through collections
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
```

---

## 4. Loop Control Statements
* `break`: Terminate the loop immediately.
* `continue`: Skip the rest of the current iteration and move to the next.

```python
for num in range(10):
    if num == 3:
        continue  # Skips 3
    if num == 7:
        break     # Stops the loop entirely
    print(num)
```

---

## 5. Hands-on Practice
Open [loop_conditions.py](file:///C:/Users/smpni/.gemini/antigravity/scratch/Code-Pathshala/src/code_pathshala/basics/loop_conditions.py) to study the classic **FizzBuzz** algorithm implementation using conditionals and loops.

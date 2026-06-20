# Lesson 5: Advanced Python Features & CPython Frame Mechanics

Welcome to Lesson 5! Here, we explore advanced python constructs—recursion, decorators, generators, and context managers—along with how CPython manages stack frames under the hood.

---

## 1. Recursion & the Call Stack
A recursive function calls itself. Every call pushes a new **stack frame** onto the CPU/RAM call stack to keep track of its local variables.

* **Base Case:** The stopping condition that prevents infinite loops.
* **Recursive Step:** The function calls itself with a simpler input.

> [!WARNING]
> If a recursive function is too deep, Python will raise a `RecursionError` (Stack Overflow) to protect memory.

---

## 2. Decorators & Closures
A **closure** is an inner function that remembers and has access to variables in its outer enclosing scope, even after the outer function has finished executing.

A **decorator** is a closure wrapper that takes a function as an argument, extends its behavior, and returns a new function, modifying its behavior without changing its source code.

```python
def my_decorator(func):
    def wrapper():
        print("Before call")
        func()
        print("After call")
    return wrapper

@my_decorator
def hello():
    print("Hello!")
```

---

## 3. Generators (`yield`)
Generators are functions that yield values one at a time lazily. Unlike standard functions that return a value and destroy their stack frame, generators use the `yield` keyword to **suspend** execution and save their local frame state in memory.

* Generators use significantly less RAM because they do not build whole list structures in memory.
* Values are requested on-demand using `next()`.

---

## 4. Context Managers (`with`)
Context managers simplify resource handling (opening files, acquiring locks) by ensuring cleanup actions run automatically, even if errors occur inside the block.

* Managed using the `with` statement.
* Implemented by defining `__enter__()` and `__exit__()` magic methods in a class.

---

## 5. Hands-on Practice
* Look through the [advanced/](file:///C:/Users/smpni/.gemini/antigravity/scratch/Code-Pathshala/src/code_pathshala/advanced/) directory to study recursion, decorators, generators, and context manager examples.
* Complete the decorator and generator challenge in [kata_advanced.py](file:///C:/Users/smpni/.gemini/antigravity/scratch/Code-Pathshala/src/code_pathshala/labs/kata_advanced.py).

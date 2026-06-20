# Lesson 4: Object-Oriented Programming & Memory Layout

Welcome to Lesson 4! In this lesson, we will transition from procedural programming to **Object-Oriented Programming (OOP)**, learning how to group data and behavior into classes, extend them via inheritance, and understand how they map into memory.

---

## 1. Class vs Object
* A **Class** is a blueprint or template for creating objects. It defines what attributes (data) and methods (functions) the objects will have.
* An **Object** is a specific instance of a class, created in the heap memory.

```python
class Dog:
    def __init__(self, name: str):
        self.name = name  # Instance attribute

    def bark(self) -> str:
        return f"{self.name} says Woof!"
```

---

## 2. Pointers & Variable Aliasing
When you assign a class instance to a variable, the variable stores a **reference pointer** to the object's address on the heap, not the object itself.

```python
dog_a = Dog("Buddy")
dog_b = dog_a
```

* `dog_b` does NOT copy the object; it points to the exact same memory address as `dog_a`.
* Modifying `dog_b` will modify `dog_a` because they reference the same heap object.
* You can check if two variables point to the same memory ID using `id(dog_a) == id(dog_b)` or `dog_a is dog_b`.

---

## 3. Inheritance & Method Overriding
Inheritance allows a new class (subclass) to inherit attributes and methods from an existing class (superclass), reducing code redundancy.

```python
class Animal:
    def speak(self):
        return "Some generic sound"

class Cat(Animal):
    def speak(self):  # Method overriding
        return "Meow"
```

Use `super().__init__(...)` to call the constructor of the parent class from within the subclass constructor.

---

## 4. Hands-on Practice
* Study [oop.py](file:///C:/Users/smpni/.gemini/antigravity/scratch/Code-Pathshala/src/code_pathshala/basics/oop.py) and [mutability.py](file:///C:/Users/smpni/.gemini/antigravity/scratch/Code-Pathshala/src/code_pathshala/basics/mutability.py) for practical implementation and copying behaviors (shallow vs deep copies).
* Open [kata_oop.py](file:///C:/Users/smpni/.gemini/antigravity/scratch/Code-Pathshala/src/code_pathshala/labs/kata_oop.py) and implement the `BankAccount` class. Run tests using:
  ```bash
  pathshala test
  ```

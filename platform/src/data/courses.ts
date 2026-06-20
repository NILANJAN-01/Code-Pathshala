export interface CourseTopic {
  id: string;
  title: string;
  track: string;
  description: string;
  internals: string;
  sourceCode: string;
  challenge: {
    description: string;
    template: string;
    solution: string;
    testCases: { input: string; expected: string }[];
  };
}

export const tracks = [
  { id: "track1", title: "🎓 Track 1: Foundations (College Level)" },
  { id: "track2", title: "🧠 Track 2: OOP & Mutability (Intermediate)" },
  { id: "track3", title: "⚙️ Track 3: Python Virtual Machine (Advanced)" },
  { id: "track4", title: "🚀 Track 4: Production & RAM Internals (Professional)" },
];

export const courseData: CourseTopic[] = [
  {
    id: "variables",
    title: "Variables and Memory Identity",
    track: "track1",
    description: "Learn how Python variables act as reference labels pointing to objects in memory rather than direct containers.",
    internals: "In Python, every variable is a pointer (C-level PyObject*). Declaring `a = 10` allocates an integer object in the heap and binds name `a` in the local namespace dict to that heap address.",
    sourceCode: `def make_profile(name: str, age: int) -> dict:
    # Variables name and age point to objects in heap
    # A dictionary object is created and returned
    return {"name": name, "age": age}`,
    challenge: {
      description: "Implement a function `swap_values(a, b)` that returns a tuple `(b, a)` showing reference swapping.",
      template: `def swap_values(a, b):
    # Write code here
    pass`,
      solution: `def swap_values(a, b):
    return b, a`,
      testCases: [
        { input: "1, 2", expected: "(2, 1)" },
        { input: "'x', 'y'", expected: "('y', 'x')" }
      ]
    }
  },
  {
    id: "strings",
    title: "String Slicing and Immutability",
    track: "track1",
    description: "Strings are immutable sequences of Unicode characters. Slicing creates new string objects in memory.",
    internals: "Because strings are immutable, modifying a string (e.g. `s += '!'`) allocates a completely new string object on the heap, copying the characters and modifying the pointer.",
    sourceCode: `def greet(name: str) -> str:
    return f"Hello, {name}!"

def shout(text: str) -> str:
    return text.upper()`,
    challenge: {
      description: "Implement `reverse_string(s)` using Python slicing to return a reversed copy of the string.",
      template: `def reverse_string(s):
    # Write code here
    pass`,
      solution: `def reverse_string(s):
    return s[::-1]`,
      testCases: [
        { input: "'python'", expected: "'nohtyp'" },
        { input: "'racecar'", expected: "'racecar'" }
      ]
    }
  },
  {
    id: "oop",
    title: "Object-Oriented Programming",
    track: "track2",
    description: "Model real-world entities using classes and objects. Understand constructors, methods, and inheritance.",
    internals: "Classes define a struct layout. Instances of classes contain a `__dict__` pointing to their attributes. Dynamic attribute lookup crawls from instance dict, class dict, up to parent class dicts.",
    sourceCode: `class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id`,
    challenge: {
      description: "Implement a class `Car` with `__init__(self, brand)` and a method `drive(self)` returning 'Driving [brand]'.",
      template: `class Car:
    # Implement constructor and drive method
    pass`,
      solution: `class Car:
    def __init__(self, brand):
        self.brand = brand
    def drive(self):
        return f"Driving {self.brand}"`,
      testCases: [
        { input: "Car('Tesla').drive()", expected: "'Driving Tesla'" },
        { input: "Car('Toyota').drive()", expected: "'Driving Toyota'" }
      ]
    }
  },
  {
    id: "mutability",
    title: "Aliasing and Copy Behaviors",
    track: "track2",
    description: "Understand the difference between naming aliases, shallow copies, and deep copies.",
    internals: "Assignment `b = a` copies the reference pointer, not the object. `a.copy()` copies the top-level list but re-uses inner pointers. `copy.deepcopy()` recursively copies all objects, creating completely isolated data structure paths.",
    sourceCode: `import copy

def demonstrate_aliasing():
    original = [1, 2, 3]
    alias = original
    alias.append(4)
    return original, alias`,
    challenge: {
      description: "Write a function `is_alias(x, y)` that returns True if x and y reference the same object in memory, False otherwise.",
      template: `def is_alias(x, y):
    # Write code here
    pass`,
      solution: `def is_alias(x, y):
    return x is y`,
      testCases: [
        { input: "[1, 2], [1, 2]", expected: "False" },
        { input: "let a = [1]; is_alias(a, a)", expected: "True" }
      ]
    }
  },
  {
    id: "recursion",
    title: "Recursion and Stack Frames",
    track: "track3",
    description: "Write self-referential recursive functions and inspect how the call stack frame accumulates parameters.",
    internals: "Every recursive call allocates a C-level Frame Object (`PyFrameObject`) on the CPU execution call stack. This frame stores arguments, local variables, and the return address. When memory runs out, it triggers RecursionError.",
    sourceCode: `def fibonacci(n: int) -> int:
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n - 1) + fibonacci(n - 2)`,
    challenge: {
      description: "Implement a recursive function `factorial(n)` returning the product of all integers up to n.",
      template: `def factorial(n):
    # Write code here
    pass`,
      solution: `def factorial(n):
    if n <= 1: return 1
    return n * factorial(n - 1)`,
      testCases: [
        { input: "5", expected: "120" },
        { input: "0", expected: "1" }
      ]
    }
  },
  {
    id: "decorators",
    title: "Closures and Decorators",
    track: "track3",
    description: "Master functions as first-class citizens, scope closures, and wrapper decorator syntax (@decorator).",
    internals: "Closures capture variables from an outer enclosing function by storing them in a `__closure__` tuple of cells. Decorators dynamically wrap functions by replacing their name pointer in the namespace dict with the inner wrapper pointer.",
    sourceCode: `def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper`,
    challenge: {
      description: "Write a decorator `double_result` that doubles the return value of any function it wraps.",
      template: `def double_result(func):
    # Write decorator code here
    pass`,
      solution: `def double_result(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper`,
      testCases: [
        { input: "@double_result\\ndef add(a, b): return a + b\\nadd(2, 3)", expected: "10" }
      ]
    }
  },
  {
    id: "refcount",
    title: "Reference Counting Internals",
    track: "track4",
    description: "Learn how CPython tracks heap structures and manages automatic memory deallocations via reference tracking.",
    internals: "Every CPython object has an `ob_refcnt` struct field. Assignments and parameters increase the count. When variables are deleted or go out of scope, the count is decremented. When count is 0, Python instantly frees the memory block.",
    sourceCode: `import sys

def get_actual_refcount(obj):
    return sys.getrefcount(obj) - 1`,
    challenge: {
      description: "Explain why passing an object to a function increases its reference count. (Self-solve: verify frame parameters references)",
      template: `# Just return True to pass after understanding.
def understand_frame_references():
    return True`,
      solution: `def understand_frame_references():
    return True`,
      testCases: [
        { input: "understand_frame_references()", expected: "True" }
      ]
    }
  },
  {
    id: "asyncio",
    title: "Asynchronous Concurrency",
    track: "track4",
    description: "Write concurrent, non-blocking code using cooperative event loops, Tasks, and async/await.",
    internals: "CPython utilizes an Event Loop that polls registered I/O tasks. When a task awaits, it yields execution control back to the loop. Coroutines suspend their state using generator yield logic under the hood.",
    sourceCode: `import asyncio

async def fetch_task(task_id: int, delay: float):
    await asyncio.sleep(delay)
    return f"Task {task_id} completed"`,
    challenge: {
      description: "Create an async function `add_async(a, b)` that sleeps for 0.05 seconds and then returns `a + b`.",
      template: `import asyncio

async def add_async(a, b):
    # Write code here
    pass`,
      solution: `import asyncio

async def add_async(a, b):
    await asyncio.sleep(0.05)
    return a + b`,
      testCases: [
        { input: "asyncio.run(add_async(5, 5))", expected: "10" }
      ]
    }
  }
];

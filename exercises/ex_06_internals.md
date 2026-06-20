# Lesson 6: Python Memory Internals & Async Cooperative Concurrency

Welcome to Lesson 6! This lesson goes deep under the hood of CPython's memory management (Reference Counting and Garbage Collection) and covers asynchronous cooperative multitasking.

---

## 1. Reference Counting
Every Python object in the heap has a reference counter (`ob_refcnt` in CPython).
* When a variable is assigned to an object, its reference count increases by 1.
* When a variable is deleted (`del`) or falls out of scope, the reference count decreases by 1.
* When the reference count reaches **0**, the memory is immediately deallocated.

You can inspect reference counts using `sys.getrefcount(obj)`.

---

## 2. Reference Cycles & Garbage Collection
A **Reference Cycle** occurs when objects reference each other in a circle (e.g. A references B, B references A), but they are no longer reachable from any variable on the stack.

* In this case, their reference counts never reach 0, causing a memory leak.
* Python resolves this using a **Cyclic Garbage Collector (GC)** that runs periodically in the background, scans for unreachable reference cycles, and sweeps them from memory.

---

## 3. Asynchronous Cooperative Concurrency
Python's `asyncio` framework enables cooperative multitasking.
* Runs on a single thread using an **Event Loop**.
* Functions defined with `async def` return coroutines.
* The `await` keyword suspends the execution of a coroutine, yielding control back to the event loop so other tasks can run in a non-blocking manner.
* Tasks are executed concurrently using `asyncio.gather()`.

---

## 4. Hands-on Practice
* Run the memory internals demo script:
  ```bash
  pathshala run-example internals
  ```
* Run the asynchronous multitasking demo:
  ```bash
  pathshala run-example async
  ```
* Open [kata_professional.py](file:///C:/Users/smpni/.gemini/antigravity/scratch/Code-Pathshala/src/code_pathshala/labs/kata_professional.py) and implement the asynchronous concurrent fetch orchestrator.

# Mentor & Teacher's Guide

This guide is designed for instructors, mentors, and teachers using **Code Pathshala** to deliver Python programming courses. It outlines the curriculum layout and offers best practices for conducting lessons, reviewing student solutions, and verifying code.

---

## 🏫 Curriculum Overview

The repository is divided into logical folders separating explanations, examples, implementation exercises, and tests:

```
├── docs/                   # Guides for Students and Teachers
├── exercises/              # Conceptual lessons (Markdown)
├── examples/               # Fully runnable demo scripts
├── src/code_pathshala/
│   ├── basics/             # Standard Python structures
│   ├── labs/               # Student templates to implement (Katas)
│   └── utils/              # Package-wide utility functions
└── tests/                  # Automated pytest test suites
```

---

## 🎓 Recommended Teaching Flow

### Step 1: Theoretical Explanation
Ask students to read the markdown guides in `exercises/` or present the contents during class. You can direct students to read them directly in the terminal:
```bash
pathshala exercise variables
```

### Step 2: Show Examples in Action
Run and walk through the scripts in `examples/`. Emphasize code structure, variable naming, library imports, and user input handling.
```bash
pathshala run-example use_utils
```

### Step 3: Student Lab Implementation (Katas)
Instruct students to complete coding exercises located in `src/code_pathshala/labs/`.
* [kata_numbers.py](file:///C:/Users/smpni/.gemini/antigravity/scratch/Code-Pathshala/src/code_pathshala/labs/kata_numbers.py) (implements factorial)
* [kata_string.py](file:///C:/Users/smpni/.gemini/antigravity/scratch/Code-Pathshala/src/code_pathshala/labs/kata_string.py) (implements reverse words and palindrome check)

### Step 4: Automated Testing
Encourage students to run the test suite periodically to verify their progress. They can run `pathshala test` or run `pytest` inside the terminal.

---

## 🔍 Code Review & Guidelines

Ensure students maintain high code quality standards. You can leverage the installed quality checking tools to inspect student code:

* **Formatting Check (`black`):** Ensure consistent python formatting.
  ```bash
  black --check src/
  ```
* **Linting Check (`ruff`):** Verify clean code standards and style guidelines.
  ```bash
  ruff check src/
  ```

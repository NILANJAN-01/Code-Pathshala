# Student Getting Started Guide

Welcome to **Code Pathshala**! This guide will walk you through setting up your local environment, using the interactive CLI, and completing the exercises.

---

## 🛠️ Prerequisites
Make sure you have **Python 3.10 or newer** installed. You can check your Python version by running:
```bash
python --version
```

---

## 🚀 Setup Steps

### 1. Create a Virtual Environment
It is highly recommended to isolate your project dependencies using a virtual environment:

```bash
# Create the environment
python -m venv .venv

# Activate it (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Activate it (Windows Command Prompt)
.venv\Scripts\activate.bat

# Activate it (Linux/macOS)
source .venv/bin/activate
```

### 2. Install Code Pathshala in Editable Mode
Install the package locally along with the development and testing packages (`pytest`, `black`, `ruff`):

```bash
pip install -e .[dev]
```
> [!NOTE]
> The `-e` flag (editable mode) ensures that any code changes you make in the package are immediately reflected in the CLI.

---

## 🖥️ Using the Interactive CLI
Code Pathshala installs a command-line tool named `pathshala`. Run it to see what commands are available:

```bash
pathshala --help
```

### 1. View Curriculum
To see all lessons, runnable examples, and coding practice Katas:
```bash
pathshala list
```

### 2. Read a Lesson
To read any of the lessons directly in your terminal:
```bash
pathshala exercise variables
pathshala exercise strings
pathshala exercise loops
```

### 3. Run Examples
Run one of the pre-made examples to see concepts in action:
```bash
pathshala run-example hello
pathshala run-example utils
pathshala run-example github
```

---

## 🎯 How to Complete Katas
1. Navigate to the `src/code_pathshala/labs/` directory.
2. Open [kata_string.py](file:///C:/Users/smpni/.gemini/antigravity/scratch/Code-Pathshala/src/code_pathshala/labs/kata_string.py) or [kata_numbers.py](file:///C:/Users/smpni/.gemini/antigravity/scratch/Code-Pathshala/src/code_pathshala/labs/kata_numbers.py).
3. Read the docstring instructions for the function.
4. Implement or modify the function.
5. Verify your solutions by running tests:
   ```bash
   pathshala test
   ```
   Or run pytest directly:
   ```bash
   pytest
   ```

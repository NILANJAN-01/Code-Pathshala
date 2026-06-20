# 📚 Code Pathshala

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A curated, open-source collection of high-quality study materials designed to facilitate a structured learning path for Python programming, from foundational concepts to advanced application. It includes a built-in interactive CLI companion to study, run examples, and test your coding skills.

---

## ✨ Features

- **Terminal-Based Learning:** Read python theory directly in your terminal using formatted Markdown.
- **Runnable Sandbox Examples:** Demo files illustrating basic and intermediate programming concepts.
- **Practice coding Katas (Labs):** Fun programming assignments to implement.
- **Automated Tests:** Verify your solutions immediately using `pytest`.
- **Quality Standards:** Configured with pre-packaged modern dev tooling (`black`, `ruff`, `mypy`).

---

## 📂 Repository Directory Structure

```
├── docs/                   # Guides for Students and Teachers
│   ├── gettingstarted.md   # Step-by-step setup for learners
│   └── teaching.md         # Framework guidelines for mentors
├── exercises/              # Conceptual lessons (Markdown)
├── examples/               # Fully runnable demo scripts
├── src/
│   └── code_pathshala/
│       ├── basics/         # core basics files
│       ├── labs/           # coding practice templates (Katas)
│       ├── utils/          # reusable standard utilities
│       └── cli.py          # interactive Typer/Rich CLI application
├── tests/                  # automated test suites
├── pyproject.toml          # packaging configuration & metadata
└── LICENSE                 # open-source MIT license
```

---

## 🚀 Setup & Installation

To get started, follow these instructions to install the package in editable mode along with development tools:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/NILANJAN-01/Code-Pathshala.git
   cd Code-Pathshala
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\Activate.ps1
   # On Linux/macOS:
   source .venv/bin/activate
   ```

3. **Install the package:**
   ```bash
   pip install -e .[dev]
   ```

---

## 🖥️ Interactive CLI Usage

Code Pathshala installs a console script called `pathshala`. Run it to explore options:

```bash
# View general instructions and package info
pathshala info

# List all available lessons, examples, and katas
pathshala list

# Open a lesson directly in the terminal
pathshala exercise strings

# Run a sample example script
pathshala run-example github

# Run tests to check your solutions
pathshala test
```

---

## 🧪 Running Tests Directly

If you prefer to run tests using standard python tools, make sure you have activated your virtual environment and run:

```bash
# Run all unit tests
pytest -v

# Run formatting checks
black --check src/

# Run linting check
ruff check src/
```

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

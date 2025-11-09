[project]
name = "code-pathshala"
version = "0.1.0"
description = "Beginner-friendly Python package with reusable utilities, exercises, tests, and mini-project templates."
readme = "README.md"
requires-python = ">=3.10"
authors = [{ name = "Nilanjan Singhamahapatra" }]
license = { text = "MIT" }
dependencies = [
  "typer>=0.12",
  "rich>=13.0",
  "python-dotenv>=1.0",
  "requests>=2.31",
]

[project.scripts]
pathshala = "code_pathshala.cli:app"

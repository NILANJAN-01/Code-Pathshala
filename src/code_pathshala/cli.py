"""
Command Line Interface (CLI) for Code Pathshala.

Run commands like:
  pathshala hello --name Student
  pathshala add 10 20
"""

import typer
from rich import print
from code_pathshala.utils import math_ops



app = typer.Typer(help="Code Pathshala – learn-by-doing CLI.")


@app.command()
def hello(name: str = "World"):
    """Say hello with style."""
    print(f"[bold green]Hello, {name}![/bold green]")


@app.command()
def add(a: float, b: float):
    """Add two numbers using reusable utils."""
    print(f"The sum of {a} and {b} is {math_ops.add(a, b)}")


@app.command()
def info():
    """Show quick package info."""
    print("[bold cyan]Modules:[/bold cyan] basics, utils, labs")
    print("[yellow]Try: pathshala hello --name You | pathshala add 2 3[/yellow]")


if __name__ == "__main__":
    app()

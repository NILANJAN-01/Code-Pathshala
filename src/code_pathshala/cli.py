"""
Command Line Interface (CLI) for Code Pathshala.
"""

import sys
import subprocess
from pathlib import Path
import typer
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from code_pathshala.utils import math_ops

# Ensure stdout/stderr use UTF-8 to prevent UnicodeEncodeError on legacy Windows console encodings
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


app = typer.Typer(
    help="Code Pathshala – An interactive CLI learning companion for Python.",
    rich_markup_mode="rich",
)
console = Console()


@app.command()
def hello(name: str = "Student"):
    """Say hello with style to the learner."""
    console.print(f"[bold green]👋 Hello, {name}![/bold green]")
    console.print(
        "Welcome to [bold cyan]Code Pathshala[/bold cyan]! Let's write some Python. 🐍"
    )


@app.command()
def add(a: float, b: float):
    """Add two numbers using reusable math utilities."""
    result = math_ops.add(a, b)
    console.print(
        f"➕ The sum of [bold green]{a}[/bold green] and [bold green]{b}[/bold green] is [bold cyan]{result}[/bold cyan]"
    )


@app.command()
def info():
    """Show detailed info about Code Pathshala packages and path."""
    console.print("[bold cyan]📚 Code Pathshala - Python Learning Platform[/bold cyan]")
    console.print("Created by [bold]Nilanjan Singhamahapatra[/bold]\n")
    console.print("[yellow]Modules available for import:[/yellow]")
    console.print(
        "  - [bold green]code_pathshala.basics[/bold green] : Variables, strings, numbers, loops, lists & dicts"
    )
    console.print(
        "  - [bold green]code_pathshala.labs[/bold green]   : Practice coding Katas (factorial, palindrome, etc.)"
    )
    console.print(
        "  - [bold green]code_pathshala.utils[/bold green]  : Reusable I/O, math operations, API utilities, timing decorator"
    )
    console.print("\n[yellow]Quick CLI commands to get started:[/yellow]")
    console.print(
        "  - [bold white]pathshala list[/bold white]         : Show all exercises, examples, and katas."
    )
    console.print(
        "  - [bold white]pathshala exercise strings[/bold white]  : Read strings exercise lesson."
    )
    console.print(
        "  - [bold white]pathshala test[/bold white]         : Run all unit tests."
    )


@app.command()
def list():
    """List all available exercises, coding katas, and runnable examples."""
    console.print("\n[bold cyan]📂 Code Pathshala - Course Curriculum[/bold cyan]\n")

    # Exercises Table
    ex_table = Table(
        title="📝 Learning Exercises", show_header=True, header_style="bold magenta"
    )
    ex_table.add_column("Key", style="cyan", width=15)
    ex_table.add_column("Description", style="white")
    ex_table.add_column("File Path", style="dim green")

    ex_table.add_row(
        "variables",
        "Basic types, variables & arithmetic operations",
        "exercises/ex_01_variables.md",
    )
    ex_table.add_row(
        "strings",
        "String operations, indexing, slicing, methods",
        "exercises/ex_02_strings.md",
    )
    ex_table.add_row(
        "loops",
        "Conditionals, loops (for/while), flow control",
        "exercises/ex_03_loops.md",
    )

    console.print(ex_table)
    console.print()

    # Examples Table
    exm_table = Table(
        title="💡 Runnable Examples", show_header=True, header_style="bold green"
    )
    exm_table.add_column("Key", style="cyan", width=15)
    exm_table.add_column("Description", style="white")
    exm_table.add_column("File Path", style="dim green")

    exm_table.add_row(
        "hello", "Classic Hello World with rich styling", "examples/hello_world.py"
    )
    exm_table.add_row(
        "utils", "Demonstrating file I/O & math utilities", "examples/use_utils.py"
    )
    exm_table.add_row(
        "github", "Fetching repositories from GitHub API", "examples/call_github_api.py"
    )

    console.print(exm_table)
    console.print()

    # Katas Table
    kata_table = Table(
        title="🎯 Practice Katas (Labs)", show_header=True, header_style="bold blue"
    )
    kata_table.add_column("Module", style="cyan", width=15)
    kata_table.add_column("Functions to Implement / Practice", style="white")
    kata_table.add_column("File Path", style="dim green")

    kata_table.add_row(
        "numbers", "factorial(n)", "src/code_pathshala/labs/kata_numbers.py"
    )
    kata_table.add_row(
        "string",
        "reverse_words(text), is_palindrome(text)",
        "src/code_pathshala/labs/kata_string.py",
    )

    console.print(kata_table)
    console.print(
        "\n💡 [dim]Use `pathshala exercise <key>` to study or `pathshala run-example <key>` to run code.[/dim]\n"
    )


@app.command()
def exercise(name: str):
    """View details of a specific exercise (e.g. variables, strings, loops)."""
    # Map name to file
    mapping = {
        "variables": "exercises/ex_01_variables.md",
        "strings": "exercises/ex_02_strings.md",
        "loops": "exercises/ex_03_loops.md",
    }

    clean_name = name.lower().strip()
    if clean_name not in mapping:
        console.print(
            f"[bold red]Error:[/bold red] Exercise '{name}' not found. Try running [bold]pathshala list[/bold] to see valid keys."
        )
        raise typer.Exit(code=1)

    root = Path(__file__).resolve().parent.parent.parent
    file_path = root / mapping[clean_name]

    if not file_path.exists():
        file_path = Path.cwd() / mapping[clean_name]

    if not file_path.exists():
        console.print(
            f"[bold red]Error:[/bold red] Exercise file not found at {file_path}"
        )
        raise typer.Exit(code=1)

    content = file_path.read_text(encoding="utf-8")
    markdown = Markdown(content)
    console.print(markdown)


@app.command(name="run-example")
def run_example(name: str):
    """Run an example python script (e.g. hello, utils, github)."""
    mapping = {
        "hello": "examples/hello_world.py",
        "utils": "examples/use_utils.py",
        "github": "examples/call_github_api.py",
    }

    clean_name = name.lower().strip()
    if clean_name not in mapping:
        console.print(
            f"[bold red]Error:[/bold red] Example '{name}' not found. Try running [bold]pathshala list[/bold] to see valid keys."
        )
        raise typer.Exit(code=1)

    root = Path(__file__).resolve().parent.parent.parent
    file_path = root / mapping[clean_name]
    if not file_path.exists():
        file_path = Path.cwd() / mapping[clean_name]

    if not file_path.exists():
        console.print(
            f"[bold red]Error:[/bold red] Example script not found at {file_path}"
        )
        raise typer.Exit(code=1)

    console.print(
        f"[bold green]Running example {mapping[clean_name]}...[/bold green]\n"
    )
    try:
        result = subprocess.run([sys.executable, str(file_path)], check=True)
        if result.returncode == 0:
            console.print(
                f"\n[bold green]Example {clean_name} executed successfully![/bold green]"
            )
    except subprocess.CalledProcessError as e:
        console.print(f"\n[bold red]Error running example:[/bold red] {e}")
        raise typer.Exit(code=e.returncode)


@app.command()
def test():
    """Run the pytest test suite and display results."""
    console.print("[bold cyan]🧪 Running Pytest Suite...[/bold cyan]\n")
    try:
        result = subprocess.run(["pytest", "-v"], check=False)
        if result.returncode == 0:
            console.print(
                "\n[bold green]✅ All tests passed successfully![/bold green]"
            )
        else:
            console.print(
                f"\n[bold red]❌ Some tests failed (Exit code: {result.returncode})[/bold red]"
            )
            raise typer.Exit(code=result.returncode)
    except FileNotFoundError:
        console.print(
            "[bold red]Error:[/bold red] `pytest` executable not found. Make sure you installed dev dependencies with `pip install -e .[dev]`"
        )
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()

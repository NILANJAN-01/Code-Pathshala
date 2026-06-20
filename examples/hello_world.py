#!/usr/bin/env python3
"""
Example: Hello World in Code-Pathshala
This script demonstrates basic CLI output styling using the `rich` library.
"""

import sys
from rich.console import Console
from rich.panel import Panel

# Ensure stdout/stderr use UTF-8 to prevent UnicodeEncodeError on legacy Windows console encodings
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

console = Console()


def main():
    # Print a styled title using a panel
    console.print(
        Panel(
            "[bold green]🐍 Welcome to Python Programming! 🐍[/bold green]\n"
            "[cyan]This is a demo script from Code Pathshala.[/cyan]",
            title="[bold yellow]Hello World Example[/bold yellow]",
            expand=False,
        )
    )

    # Basic prints with color markup
    console.print("Let's look at some formatting:")
    console.print("- This text is [bold red]bold and red[/bold red].")
    console.print("- This text is [italic blue]italicized and blue[/italic blue].")
    console.print(
        "- This is a [black on yellow]warning-style banner[/black on yellow].\n"
    )

    # Ask the user for input using rich console
    name = console.input("[bold magenta]What is your name? [/bold magenta]")

    if not name.strip():
        name = "Python Enthusiast"

    # Print a beautiful personalized greeting
    console.print(
        f"\n✨ Hello, [bold green]{name}[/bold green]! You are ready to start your learning journey! ✨"
    )


if __name__ == "__main__":
    main()

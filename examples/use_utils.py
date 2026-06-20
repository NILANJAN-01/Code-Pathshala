#!/usr/bin/env python3
"""
Example: Using Package Utilities
This script demonstrates how to import and use internal package utilities like
custom math functions, file I/O operations, and the performance decorator.
"""

import sys
from pathlib import Path
from code_pathshala.utils.math_ops import mean, divide
from code_pathshala.utils.io import write_text, read_text
from code_pathshala.utils.timing import timed
from rich.console import Console

# Ensure stdout/stderr use UTF-8 to prevent UnicodeEncodeError on legacy Windows console encodings
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

console = Console()


@timed
def process_numbers(nums: list[float]) -> float:
    """A sample function decorated with @timed to measure its execution time."""
    console.print(f"[dim]Processing {len(nums)} values...[/dim]")
    return mean(nums)


def main():
    console.print("[bold cyan]🔧 Reusable Utilities Demo[/bold cyan]\n")

    # 1. Using Math Utilities
    numbers = [10.5, 20.0, 30.25, 40.0, 50.75]
    avg = process_numbers(numbers)
    console.print(f"📊 The average of the values is: [bold green]{avg}[/bold green]")

    try:
        divide(10, 0)
    except ZeroDivisionError as e:
        console.print(f"❌ Division safety check: [italic red]{e}[/italic red]")

    # 2. Using I/O Utilities
    console.print("\n💾 Testing safe File I/O operations:")
    temp_file = Path("scratch/temp_demo.txt")
    demo_content = (
        "Hello, this is a file write/read operation using code_pathshala.utils.io!"
    )

    # Write
    write_text(temp_file, demo_content)
    console.print(f"✔️ Successfully wrote text to: [dim green]{temp_file}[/dim green]")

    # Read
    read_data = read_text(temp_file)
    console.print(f"✔️ Successfully read text from file: [italic]{read_data}[/italic]")

    # Clean up temp file
    if temp_file.exists():
        temp_file.unlink()
        console.print("[dim]Cleaned up temporary demonstration file.[/dim]")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Example: OOP and Mutability in action
This script demonstrates how custom classes behave and how objects are referenced in memory.
"""

import sys
from code_pathshala.basics.oop import Student, introduce_person
from code_pathshala.basics.mutability import (
    demonstrate_aliasing,
    demonstrate_shallow_copy,
    demonstrate_deep_copy,
)
from rich.console import Console
from rich.panel import Panel

# Ensure stdout/stderr use UTF-8
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

console = Console()


def main():
    console.print(Panel("[bold cyan]🧬 OOP & Mutability Sandbox Demo[/bold cyan]"))

    # 1. OOP Demonstration
    console.print(
        "\n[bold yellow]1. Object-Oriented Programming (Polymorphism):[/bold yellow]"
    )
    student = Student("John Doe", 20, "S99102")
    student.enroll("Python 101")
    student.enroll("Data Structures")

    console.print(f"Created student object: [bold green]{student}[/bold green]")
    console.print(f"Enrolled courses: [bold]{', '.join(student.courses)}[/bold]")
    console.print(f"Introduction: {introduce_person(student)}")

    # 2. Mutability & Aliasing
    console.print(
        "\n[bold yellow]2. Variable Aliasing & Identity in RAM:[/bold yellow]"
    )
    orig, alias, is_same = demonstrate_aliasing()
    console.print(f"Original: {orig} | Alias: {alias}")
    console.print(
        f"Point to same memory address (id)? [bold]{is_same}[/bold] (Notice both changed!)"
    )

    # 3. Copies
    console.print(
        "\n[bold yellow]3. Shallow Copy vs Deep Copy in memory:[/bold yellow]"
    )
    orig_s, shallow, outer_same_s, inner_same_s = demonstrate_shallow_copy()
    console.print(f"Shallow Copy Outer changed? Original: {orig_s} | Copy: {shallow}")
    console.print(f"Nested element has same identity? [bold]{inner_same_s}[/bold]")

    orig_d, deep, outer_same_d, inner_same_d = demonstrate_deep_copy()
    console.print(f"Deep Copy Outer changed? Original: {orig_d} | Copy: {deep}")
    console.print(
        f"Nested element has same identity? [bold]{inner_same_d}[/bold] (Completely isolated!)"
    )


if __name__ == "__main__":
    main()

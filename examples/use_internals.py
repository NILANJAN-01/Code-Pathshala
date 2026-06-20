#!/usr/bin/env python3
"""
Example: Python Memory Internals (Reference Counting and Garbage Collection)
This script demonstrates reference counting history and cyclic garbage collections.
"""

import sys
from code_pathshala.internals.refcount_demo import trace_reference_counts
from code_pathshala.internals.gc_demo import create_and_collect_cycle
from rich.console import Console

# Ensure stdout/stderr use UTF-8
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

console = Console()


def main():
    console.print("[bold cyan]💾 Python Memory Internals Demo[/bold cyan]\n")

    # 1. Reference Counting
    console.print("[bold yellow]1. Tracking Reference Counts:[/bold yellow]")
    history = trace_reference_counts()
    console.print(
        f"- Declared unique list object (x): Refcount = [bold green]{history[0]}[/bold green]"
    )
    console.print(
        f"- Assigned alias (y): Refcount = [bold green]{history[1]}[/bold green]"
    )
    console.print(
        f"- Assigned second alias (z): Refcount = [bold green]{history[2]}[/bold green]"
    )
    console.print(
        f"- Deleted alias (z): Refcount = [bold green]{history[3]}[/bold green]"
    )
    console.print(
        f"- Deleted alias (y): Refcount = [bold green]{history[4]}[/bold green]"
    )

    # 2. Garbage Collection
    console.print("\n[bold yellow]2. Cyclic Reference Sweeps:[/bold yellow]")
    console.print(
        "Creating reference cycle: Node A <---> Node B and orphaning references..."
    )
    collected_count = create_and_collect_cycle()
    console.print(
        f"✔️ GC sweep identified and reclaimed [bold green]{collected_count}[/bold green] unreachable objects in cycle!"
    )


if __name__ == "__main__":
    main()

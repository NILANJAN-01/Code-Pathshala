#!/usr/bin/env python3
"""
Example: Asynchronous cooperative concurrency
This script demonstrates concurrent executions using asyncio.
"""

import sys
import asyncio
from code_pathshala.professional.async_demo import run_concurrent_fetches
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
    console.print("[bold cyan]⚡ Running Asynchronous Fetch Tasks...[/bold cyan]\n")

    # Run the event loop
    results, elapsed = asyncio.run(run_concurrent_fetches())

    for r in results:
        console.print(f"✔️ Received: [green]{r}[/green]")

    console.print(
        f"\n⏱️ Total Concurrency Duration: [bold yellow]{elapsed:.4f} seconds[/bold yellow]"
    )
    console.print(
        "[dim](Task delays were 0.5s, 1.0s, and 0.2s. Synchronous would be 1.7s, but concurrent is ~1.0s!)[/dim]"
    )


if __name__ == "__main__":
    main()

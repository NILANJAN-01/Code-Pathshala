#!/usr/bin/env python3
"""
Example: Fetching GitHub Repositories
This script demonstrates how to make HTTP requests, parse JSON responses,
and format the output in a clean, visual console table using `rich`.
"""

import sys
import requests
from code_pathshala.utils.net import get_json
from rich.console import Console
from rich.table import Table

# Ensure stdout/stderr use UTF-8 to prevent UnicodeEncodeError on legacy Windows console encodings
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

console = Console()


def fetch_github_repos(username: str):
    """Fetch public repositories for a given GitHub username and display them in a table."""
    url = f"https://api.github.com/users/{username}/repos?per_page=10&sort=updated"

    console.print(
        f"[bold cyan]🔍 Fetching latest 10 repositories for user:[/bold cyan] [bold yellow]{username}[/bold yellow]..."
    )

    try:
        repos = get_json(url)

        if not repos:
            console.print(
                f"[bold yellow]No public repositories found for user {username}.[/bold yellow]"
            )
            return

        # Initialize the Table
        table = Table(
            title=f"📦 GitHub Repositories for {username}",
            show_header=True,
            header_style="bold magenta",
        )
        table.add_column("Repository Name", style="cyan")
        table.add_column("Description", style="white")
        table.add_column("Stars ⭐", justify="right", style="green")
        table.add_column("Language 💻", style="blue")
        table.add_column("Last Updated 📅", style="dim")

        # Populate rows
        for repo in repos:
            name = repo.get("name", "N/A")
            description = repo.get("description") or "No description provided."
            stars = str(repo.get("stargazers_count", 0))
            language = repo.get("language") or "Unknown"
            # Format update date (YYYY-MM-DD)
            updated_at = repo.get("updated_at", "")[:10]

            table.add_row(name, description, stars, language, updated_at)

        console.print()
        console.print(table)
        console.print()

    except requests.exceptions.HTTPError as e:
        if e.response is not None and e.response.status_code == 404:
            console.print(
                f"\n[bold red]Error:[/bold red] GitHub user [bold white]'{username}'[/bold white] not found."
            )
        elif e.response is not None and e.response.status_code == 403:
            console.print(
                "\n[bold red]Error:[/bold red] GitHub API rate limit exceeded. Please try again later."
            )
        else:
            console.print(f"\n[bold red]HTTP Error occurred:[/bold red] {e}")
    except requests.exceptions.ConnectionError:
        console.print(
            "\n[bold red]Network Error:[/bold red] Unable to connect to GitHub. Please check your internet connection."
        )
    except Exception as e:
        console.print(f"\n[bold red]An unexpected error occurred:[/bold red] {e}")


def main():
    username = "NILANJAN-01"
    if len(sys.argv) > 1:
        username = sys.argv[1]

    fetch_github_repos(username)


if __name__ == "__main__":
    main()

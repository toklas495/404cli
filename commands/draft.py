import typer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import json
from typing import Optional

from utils.api import get_draft_hacks  # Ensure it returns {"data": [...]} or handles errors internally

app = typer.Typer()
console = Console()

def print_error(message: str, json_output: bool = False):
    """Prints an error message depending on the output mode."""
    error_data = {"error": message}
    if json_output:
        typer.echo(json.dumps(error_data))
    else:
        console.print(f"[red]❌ Error:[/red] {message}")
    raise typer.Exit(code=1)

@app.command("draft")
def draft_hack(
    page: Optional[int] = typer.Option(None, "--page", "-p", help="Page number of results"),
    limit: Optional[int] = typer.Option(None, "--limit", "-l", help="Limit number of results"),
    json_output: bool = typer.Option(False, "--json", help="Output raw JSON instead of styled view."),
):
    try:
        results = get_draft_hacks(page=page, limit=limit)

        if not results or not results.get("data"):
            print_error("No matching hacks found.", json_output)

        data = results["data"]

        if json_output:
            typer.echo(json.dumps(data, indent=2))
            return

        for hack in data:
            title = hack.get("title", "Untitled")
            slug = hack.get("slug", "unknown")
            username = hack.get("author", {}).get("username", "unknown")
            description = hack.get("description", "")

            panel_content = Text.from_markup(
                f"[bold cyan]{title}[/bold cyan]\n"
                f"[dim]Slug:[/dim] {slug}\n"
                f"[dim]User:[/dim] @{username}"
            )

            if description:
                panel_content.append(Text.from_markup(f"\n[bold yellow]📝 {description.strip()}[/bold yellow]"))

            console.print(Panel(panel_content, border_style="green"))

    except typer.Exit:
        raise  # Let typer handle clean exit, don't catch it
    except Exception as e:
        print_error(f"Unexpected error: {str(e)}", json_output)

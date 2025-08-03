import typer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import json

from utils.api import search_hacks

app = typer.Typer()
console = Console()

@app.command("search")
def search_hack(
    query: str = typer.Argument(None, help="Free text or advanced query (e.g., author:nimesh&&title:jwt)"),
    tag: str = typer.Option(None, "--tag", help="Search hacks by tag"),
    limit: str = typer.Option(None, "--limit", help="Search pagination"),
    json_output: bool = typer.Option(False, "--json", help="Output raw JSON instead of styled view.")
):
    try:
        if not any([query,tag]):
            console.print("[yellow]⚠️ Provide a query or at least one filter: --title, --tag, --author[/yellow]")
            raise typer.Exit()

        # Build query string
        q = query
        # Fetch results
        results = search_hacks(tag=tag, q=q, limit=limit)["data"]
        if not results:
            console.print("[red]❌ No matching hacks found.[/red]")
            raise typer.Exit()

        if json_output:
            typer.echo(json.dumps(results, indent=2))
            raise typer.Exit()

        # Render each result
        for hack in results:
            title = hack.get("title", "Untitled")
            slug = hack.get("slug", "unknown")
            username = hack.get("author", {}).get("username", "unknown")
            content = hack.get("description", "")  # First line as description

            panel_content = Text.from_markup(
                f"[bold cyan]{title}[/bold cyan]\n"
                f"[dim]Slug:[/dim] {slug}\n"
                f"[dim]User:[/dim] @{username}"
            )

            if content:
                panel_content.append(Text.from_markup(f"\n[bold yellow]📝 {content.strip()}[/bold yellow]", style=""))

            console.print(Panel(panel_content, border_style="green"))

    except Exception as e:
        console.print(f"[red]❌ Error:[/red] {str(e)}")

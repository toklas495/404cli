import typer
from rich.console import Console
from rich.panel import Panel
from utils.display import render_hack

from utils.api import get_hack_by_id, get_hack_by_slug
from utils.meta import load_last_hack_id
from utils.format import format_date

import subprocess
from io import StringIO

app = typer.Typer()
console = Console()

@app.command("read")
def read_hack(
    id: str = typer.Option(None, "--id", "-i", help="Read your private hack by ID. Uses last pushed if not provided."),
    slug: str = typer.Option(None, "--slug", help="Read a public hack by slug.")
    
):
    try:
        # Determine if we're using slug or ID
        if slug:
            slug_hack = get_hack_by_slug(slug)["data"]
            hack = {
                "id":slug_hack["id"],
                "title":slug_hack["title"],
                "tags":slug_hack["social"].get("tags"),
                "author_name":slug_hack["author"].get("username"),
                "created_at":slug_hack["created_at"],
                "content":slug_hack["content"]
            }
            source = f"slug: {slug}"
        else:
            hack_id = id or load_last_hack_id()
            if not hack_id:
                console.print("[red]❌ No ID provided and no previous hack found.[/red]")
                raise typer.Exit()
            hack = get_hack_by_id(hack_id)["data"]
            hack["author_name"] = "me"
            source = f"id: {hack_id}"

        # Prepare metadata table
        render_hack(hack,"online")

    except Exception as e:
        console.print(Panel.fit(
            f"[red]{str(e)}[/red]",
            title="[bold red]Read Failed[/bold red]",
            border_style="red"
        ))

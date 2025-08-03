import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown
from rich.text import Text
from rich.console import Group

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
        meta_table = Table.grid(padding=(0, 1))
        meta_table.add_column(justify="right", style="bold cyan")
        meta_table.add_column()

        meta_table.add_row("🏴 Title:", hack.get("title", "N/A"))
        meta_table.add_row("🏷️ Tags:", ", ".join(hack.get("tags", [])))
        meta_table.add_row("📄 Status:", hack.get("status", "N/A"))
        meta_table.add_row("🧑 Author:", hack.get("author_name", "N/A"))
        meta_table.add_row("🕒 Created:", format_date(hack.get("created_at", "N/A")))
        meta_table.add_row("🕒 Updated:", format_date(hack.get("updated_at", "N/A")))

        meta_panel = Panel(meta_table, title=f"[green]404 Hack ({source})[/green]", border_style="green")

        # Content
        markdown = Markdown(hack.get("content", ""))
        group = Group(meta_panel, Text.from_markup("\n👨‍💻 [bold yellow]Content:[/bold yellow]\n"), markdown)

        # Display via less
        output_buffer = StringIO()
        temp_console = Console(file=output_buffer, force_terminal=True, width=100)
        temp_console.print(group)
        subprocess.run(["less", "-R"], input=output_buffer.getvalue().encode())

    except Exception as e:
        console.print(Panel.fit(
            f"[red]{str(e)}[/red]",
            title="[bold red]Read Failed[/bold red]",
            border_style="red"
        ))

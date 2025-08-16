import typer
from rich import print
from rich.console import Console
from rich.panel import Panel
from utils.file_parser import read_markdown_file,parse_markdown_file
from utils.api import post_hack
from utils.meta import save_last_hack_id

app = typer.Typer()
console = Console()

@app.command("push")
def push_hack(
    file: str = typer.Argument(..., help="Path to your markdown file"),
    draft: bool = typer.Option(False, "--draft", help="Push as draft")
):
    try:
        if not file.endswith(".md"):
            raise typer.BadParameter("Only .md files are allowed.")

        lines = read_markdown_file(file);
        hack = parse_markdown_file(lines);
        hack["status"] = "draft" if draft else "published"

        result = post_hack(hack)
        hack_id = result["data"].get("id", "unknown")

        save_last_hack_id(hack_id);
        console.print(Panel.fit(
            f"[bold green]✅ Hack pushed successfully![/bold green]\n\n[bold]ID:[/bold] {hack_id}\n[bold]Status:[/bold] {hack['status']}",
            title="[bold blue]Push Complete[/bold blue]",
            border_style="green"
        ))
    except Exception as e:
        console.print(Panel.fit(
            f"[red]❌ Error:[/red] {str(e)}",
            title="[bold red]Push Failed[/bold red]",
            border_style="red"
        ))

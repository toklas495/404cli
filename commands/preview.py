import typer
from rich import print
from rich.console import Console
from rich.panel import Panel
from utils.file_parser import read_markdown_file,parse_markdown_file
from utils.display import render_hack;
app = typer.Typer();
console = Console();

@app.command("preview")
def preview_hack(
    file: str=typer.Argument(...,help="Path to your markdown file")
):
    try:
        if not file.endswith(".md"):
            raise typer.BadParameter("Only .md files are allowed.")
        lines = read_markdown_file(file);
        hack = parse_markdown_file(lines);
        render_hack(hack);
    except Exception as e:
        console.print(Panel.fit(
            f"[red]❌ Error:[/red] {str(e)}",
            title="[bold red]preview Failed[/bold red]",
            border_style="red"
        ))
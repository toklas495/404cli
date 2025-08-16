from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown
from rich.text import Text
from io import StringIO
import subprocess

from utils.format import format_date


def render_hack(hack: dict, source: str = "local"):
    """
    Render hack metadata + content and display using less.
    Works for both local preview and remote read.
    """

    # Metadata table
    meta_table = Table.grid(padding=(0, 1))
    meta_table.add_column(justify="right", style="bold cyan", no_wrap=True)
    meta_table.add_column(style="bright_white")

    meta_table.add_row("🏴 Title", f"[bold bright_white]{hack.get('title', 'N/A')}[/bold bright_white]")
    meta_table.add_row("🏷️ Tags", f"[blue]{', '.join(hack.get('tags', [])) or '—'}[/blue]")
    meta_table.add_row("📄 Status", f"[green]{hack.get('status', 'N/A')}[/green]")
    meta_table.add_row("🧑 Author", f"[bright_white]{hack.get('author_name', 'N/A')}[/bright_white]")
    meta_table.add_row("🕒 Created", f"[dim]{format_date(hack.get('created_at', 'N/A'))}[/dim]")
    meta_table.add_row("📝 Updated", f"[dim]{format_date(hack.get('updated_at', 'N/A'))}[/dim]")

    meta_panel = Panel(
        meta_table,
        title=f"[bold cyan]📦 404 Hack[/bold cyan]",
        subtitle=f"[dim]Source: {source}[/dim]",
        border_style="cyan",
        padding=(1, 2),
    )

    # Content section
    content_header = Text.from_markup("\n👨‍💻 [bold cyan]Content[/bold cyan]\n")
    markdown = Markdown(hack.get("content", "").strip() or "_No content available._")

    group = Group(meta_panel, content_header, markdown)

    # Display via less (scrollable)
    output_buffer = StringIO()
    temp_console = Console(file=output_buffer, force_terminal=True, width=100)
    temp_console.print(group)

    subprocess.run(["less", "-R"], input=output_buffer.getvalue().encode())

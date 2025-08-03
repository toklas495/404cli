import typer
from rich import print
from rich.console import Console
from rich.panel import Panel
from utils.api import who_ami
from utils.format import format_date;

app = typer.Typer()
console = Console()

@app.command("whoami")
def whoami():
    try:
        result = who_ami()
        data = result.get("data", result)  # safe fallback
        username = data.get("username", "unknown")
        email = data.get("email", "no-email")
        score = data.get("hacker_score",0)
        created = format_date(data.get("created_at", "unknown"))

        console.print(Panel.fit(
            f"[green]Username:[/green] {username}\n"
            f"[cyan]Email:[/cyan] {email}\n"
            f"[cyan]Score:[/cyan] {score}\n"
            f"[yellow]Joined:[/yellow] {created}",
            title="[bold green]404 User Info[/bold green]",
            border_style="green"
        ))
    except Exception as e:
        console.print(Panel.fit(
            f"[red]❌ Error:[/red] {str(e)}",
            title="[bold red]whoami Failed[/bold red]",
            border_style="red"
        ))

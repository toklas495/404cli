import typer
from utils.config import save_token
from utils.token import is_valid_token

app = typer.Typer()

@app.command("set")
def set_cli_token(
    token: str = typer.Option(..., "--token", "-t", help="Your CLI token (starts with cli_)")
):
    if not is_valid_token(token):
        typer.echo("❌ Invalid token format. It should start with cli_ and be 68 chars.")
        raise typer.Exit()

    save_token(token)
    typer.echo("✅ Token saved successfully.")

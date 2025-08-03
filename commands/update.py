import typer
from rich.console import Console
from rich.panel import Panel

from utils.api import get_hack_by_id, update_hack_by_id
from utils.file_parser import parse_markdown_string
from utils.editor import open_in_editor
from utils.meta import load_last_hack_id

app =typer.Typer();
console = Console();

@app.command("update")
def update(
    id:str=typer.Option(None,"--id","-i",help="Hack ID to update"),
    draft: bool = typer.Option(False, "--draft", help="Save updated hack as a draft instead of publishing")
):
    hack_id = id or load_last_hack_id()
    if not hack_id:
        console.print("[red]❌ No ID provided and no previous hack found.[/red]")
        raise typer.Exit()
    try:
        hack = (get_hack_by_id(hack_id))["data"];

        # Construct initial content
        tags = ", ".join(hack.get("tags",[]));
        initial = f"# {hack['title']}\n> tags: {tags}\n\n{hack['content']}"

        edited = open_in_editor(initial);
        parsed = parse_markdown_string(edited);

        edited_hack = {
            "title":parsed["title"],
            **({"tags":parsed["tags"]} if parsed["tags"]!=hack["tags"] else {}),
            "content":parsed["content"]
        }

        if(len(edited_hack)==0):
            return;

        edited_hack["status"] =  "draft" if draft else "published"

        update_hack_by_id(hack_id,edited_hack);

        console.print(Panel.fit(
            f"[green]✅ Hack updated successfully![/green]\n[bold]Title:[/bold] {parsed['title']}",
            title=f"[bold green]Hack: {id}[/bold green]",
            border_style="green"
        ));


    except Exception as e:
        console.print(Panel.fit(
            f"[red]❌ {str(e)}[/red]",
            title="[bold red]Update Failed[/bold red]",
            border_style="red"
        ));

import typer
from commands import set,push,whoami,read,update,search;

app = typer.Typer()

app.add_typer(set.app);
app.add_typer(push.app);
app.add_typer(whoami.app);
app.add_typer(read.app);
app.add_typer(update.app);
app.add_typer(search.app);

if __name__=="__main__":
    app();
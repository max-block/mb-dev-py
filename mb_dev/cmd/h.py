import typer

from mb_dev.cmd import app
from mb_dev.utils import shell


@app.command(name="l", help="List servers")
def list_servers():
    shell("hcloud server list -o columns=name,ipv4,datacenter,status,type,volumes")


@app.command(name="r", help="Rebuild a server")
def rebuild_server(server: str):
    if server != "test":
        confirm = input("Sure? Type the server name again: ")
        if server != confirm:
            typer.secho("Confirm failed!", fg=typer.colors.BRIGHT_RED)
            raise typer.Exit()
    shell(f"hcloud server rebuild '{server}' --image=ubuntu-20.04")


@app.command(name="d", help="Delete a server")
def delete_server(server: str):
    confirm = input("Sure? Type the server name again: ")
    if server != confirm:
        typer.secho("Confirm failed!", fg=typer.colors.BRIGHT_RED)
        raise typer.Exit()
    shell(f"hcloud server delete '{server}'")


if __name__ == "__main__":
    app()

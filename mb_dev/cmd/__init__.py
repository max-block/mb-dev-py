import typer

from mb_dev import __version__


def version_callback(value: bool):
    if value:
        typer.echo(f"v{__version__}")
        raise typer.Exit()


app = typer.Typer(add_completion=False)


@app.callback()
def main(
    _version: bool = typer.Option(
        None,
        "--version",
        callback=version_callback,
        is_eager=True,
    ),
):
    pass

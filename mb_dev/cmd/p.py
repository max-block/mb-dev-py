import os
from pathlib import Path
from typing import Optional

import psutil
import typer

from mb_dev.cmd import app
from mb_dev.utils import shell


@app.command(name="o", help="pip3 list -o")
def pip_list_outdated():
    shell("pip3 list -o")


@app.command(name="l", help="pip3 list")
def pip_list():
    shell("pip3 list")


@app.command(name="u", help="pip3 install -U pip setuptools wheel")
def update_pip():
    shell("pip3 install -U pip setuptools wheel")


@app.command(name="i", help="install packages or project (setup.py or requirements.txt)")
def install(packages: Optional[str] = typer.Argument(None)):
    if not os.getenv("VIRTUAL_ENV"):
        typer.secho("venv is not activated")
        exit(1)

    if packages:
        shell(f"pip3 install {packages}")
        return

    if Path("setup.py").is_file():
        shell("pip3 install -Ue .[dev]")
        return

    shell("pip3 install -Ur requirements.txt")


@app.command(name="v", help="create or activate virtualenv")
def venv():
    if os.getenv("VIRTUAL_ENV"):
        typer.secho("venv is activated already")
        exit(1)

    if not Path(".venv").exists():
        shell("python3 -m venv .venv")


@app.command(name="d", help="uninstall all packages(+editable) from venv")
def uninstall():
    if not os.getenv("VIRTUAL_ENV"):
        typer.secho("venv is not activated")
        exit(1)
    shell("pip3 list --format freeze -e | xargs pip uninstall -y")
    shell("pip3 freeze | xargs pip uninstall -y")


@app.command(name="k", help="kill a dev uvicorn server")
def kill_uvicorn_server():
    for proc in psutil.process_iter(["cmdline"]):
        cmdline = proc.info["cmdline"]
        if cmdline and "uvicorn" in "".join(cmdline):
            proc.kill()
            typer.echo("done")
            return

    typer.echo("uvicorn not found")


if __name__ == "__main__":
    app()

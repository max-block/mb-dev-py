import typer

from mb_dev.cmd import app
from mb_dev.utils import shell


@app.command(name="d", help="git diff")
def diff():
    shell("git diff")


@app.command(name="l", help="git log")
def log():
    shell("git log")


@app.command(name="t", help="git tag")
def tag():
    shell("git tag --sort=-creatordate")


@app.command(name="s", help="git status")
def status():
    shell("git status")


@app.command(name="c", help="git clone")
def clone(repo: str):
    shell(f"git clone {repo}")


@app.command(name="p", help="git add & commit & push")
def push(message: str = typer.Argument("update")):
    shell(f"git add . && git commit -m '{message}' && git push")


@app.command(name="at", help="add tag local and push")
def add_tag(version: str):
    shell(f"git tag -a '{version}' -m '{version}' && git push origin {version}")


@app.command(name="dt", help="delete tag local and push")
def delete_tag(version: str):
    shell(f"git tag -d '{version}' && git push origin :refs/tags/{version}")


if __name__ == "__main__":
    app()

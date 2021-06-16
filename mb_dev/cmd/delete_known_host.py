import socket

from typer import Typer

from mb_dev.utils import shell

app = Typer(add_completion=False)


@app.command(help="Delete records from .ssh/known_hosts")
def main(host: str):
    shell(f"ssh-keygen -R {host}")
    try:
        ip = socket.gethostbyname(host)
        shell(f"ssh-keygen -R {ip}")
    except socket.gaierror:
        pass


if __name__ == "__main__":
    app()

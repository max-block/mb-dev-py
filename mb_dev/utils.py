import sys

import pexpect
import typer


def shell(cmd: str, timeout=300):
    typer.echo(cmd)
    child = pexpect.spawn("bash", ["-c", cmd], encoding="utf-8", timeout=timeout)
    child.logfile = sys.stdout
    child.expect(pexpect.EOF)

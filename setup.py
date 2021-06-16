import codecs
import os
import re

import setuptools


def find_version(*file_paths):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *file_paths), "r") as fp:
        version_file = fp.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name="mb-dev",
    version=find_version("mb_dev/__init__.py"),
    python_requires=">=3.9",
    packages=["mb_dev"],
    install_requires=["typer==0.3.2", "pexpect==4.8.0", "psutil==5.8.0"],
    extras_require={"dev": ["pytest==6.2.1", "pre-commit==2.9.3", "PySnooper==0.4.2", "wheel==0.36.2", "twine==3.3.0"]},
    entry_points={
        "console_scripts": [
            "delete_known_host = mb_dev.cmd.delete_known_host:app",
            "g = mb_dev.cmd.g:app",
            "h = mb_dev.cmd.h:app",
            "p = mb_dev.cmd.p:app",
        ],
    },
    include_package_data=True,
)

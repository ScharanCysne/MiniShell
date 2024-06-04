# MiniShell v0

import os
import sys


# List of valid commands
BUILTIN_COMMANDS = ["echo", "exit", "type", "pwd"]
PATH = os.environ.get("PATH", "/usr/bin:/usr/local/bin")


def print(string: str) -> None:
    """Overrides python's built-in print command for a sys.stdout.write command.

    Args:
        string (str): String to be written in stdout.
    """
    sys.stdout.write(string)
    sys.stdout.write("\n")

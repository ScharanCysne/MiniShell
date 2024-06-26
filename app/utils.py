# MiniShell v0

import os
import sys


# List of valid commands
BUILTIN_COMMANDS = ["echo", "exit", "type", "pwd", "cd"]
PATH = os.environ.get("PATH", "/usr/bin:/usr/local/bin")
HOME = os.environ.get("HOME", "/home")


def print(string: str) -> None:
    """Overrides python's built-in print command for a sys.stdout.write command.

    Args:
        string (str): String to be written in stdout.
    """
    sys.stdout.write(string)
    sys.stdout.write("\n")

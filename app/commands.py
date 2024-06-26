# MiniShell v0

import os
from typing import List

from .utils import BUILTIN_COMMANDS, PATH, HOME, print


def echo_command(args: List[str]) -> None:
    """MiniShell's `echo` command.

    Args:
        args (List[str]): List of arguments passed for command.
    """
    print(" ".join(args[1:]))


def type_command(args: List[str]) -> None:
    """MiniShell's `type` command.

    Args:
        args (List[str]): List of arguments passed for command.
    """
    # Get command to evaluate
    cmd = args[1]

    # Check for builtin command
    if cmd in BUILTIN_COMMANDS:
        print(f"{cmd} is a shell builtin")
    # Check for local program
    else:
        cmd_path = ""
        for os_path in PATH.split(":"):
            if os.path.isfile(f"{os_path}/{cmd}"):
                cmd_path = f"{os_path}/{cmd}"

        if cmd_path:
            print(f"{cmd} is {cmd_path}")
        else:
            print(f"{cmd} not found")


def pwd_command() -> None:
    """MiniShell's `pwd` command."""
    print(os.getcwd())


def cd_command(args: List[str]) -> None:
    """MiniShell's `cd` command.

    Args:
        args (List[str]): List of arguments passed for command.
    """
    path = args[1]
    path = path.replace("~", HOME)

    if os.path.isdir(path):
        os.chdir(path)
    else:
        print(f"cd: {path}: No such file or directory")

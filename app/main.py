import os
import sys

from typing import List

# List of valid commands
COMMANDS = ["echo", "exit", "type"]
PATH = os.environ.get("PATH", "/usr/bin:/usr/local/bin")


def echo_command(args: List[str]) -> None:
    sys.stdout.write(" ".join(args))
    sys.stdout.write("\n")


def type_command(args: List[str]) -> None:
    if args[0] in COMMANDS:
        sys.stdout.write(f"{args[0]} is a shell builtin")
        sys.stdout.write("\n")
    else:
        # Check if command in PATH
        cmd_path = ""
        for os_path in PATH.split(":"):
            if os.path.isfile(f"{os_path}/{args[0]}"):
                cmd_path = f"{os_path}/{args[0]}"

        if cmd_path:
            sys.stdout.write(f"{args[0]} is {cmd_path}")
            sys.stdout.write("\n")
        else:
            sys.stdout.write(f"{args[0]}: command not found")
            sys.stdout.write("\n")


def main():
    """MiniShell"""

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()
        args = ""

        # Check for arguments
        if " " in command:
            kws = command.split(" ")
            command = kws[0]
            args = kws[1:]

        # Check for invalid commands
        if command not in COMMANDS:
            sys.stdout.write(f"{command}: command not found\n")

        # Check for exit command
        if command == "exit" and args and args[0] == "0":
            return

        # Check for echo command
        if command == "echo" and args:
            echo_command(args)

        # Check for echo command
        if command == "type" and args:
            type_command(args)


if __name__ == "__main__":
    main()

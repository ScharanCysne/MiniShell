# MiniShell v0

import os
import sys

from .utils import BUILTIN_COMMANDS, PATH, print
from .commands import echo_command, type_command, pwd_command, cd_command


def main():
    """MiniShell"""

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input().split(" ")

        # Check for builtin command
        if command[0] in BUILTIN_COMMANDS:
            # Check for echo command
            if command[0] == "echo":
                echo_command(command)

            # Check for type command
            if command[0] == "type":
                type_command(command)

            # Check for pwd command
            if command[0] == "pwd":
                pwd_command()

            # Check for pwd command
            if command[0] == "cd":
                cd_command(command)

            # Check for exit command
            if command[0] == "exit":
                if len(command) > 1 and command[1] == "0":
                    return
                else:
                    print("exit: missing exit code")

        # Check for local program
        command_path = ""
        for os_path in PATH.split(":"):
            if os.path.isfile(f"{os_path}/{command[0]}"):
                command_path = f"{os_path}/{command[0]}"

        # Execute local program is found
        if command[0] not in BUILTIN_COMMANDS and command_path:
            os.system(" ".join(command))

        # Invalid command
        if command[0] not in BUILTIN_COMMANDS and not command_path:
            sys.stdout.write(f"{command[0]}: command not found\n")


if __name__ == "__main__":
    main()

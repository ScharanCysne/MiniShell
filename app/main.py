import sys
from typing import List

# List of valid commands
COMMANDS = ["ls", "echo", "mkdir", "exit", "type"]


def echo_command(args: List[str]):
    sys.stdout.write(" ".join(args))
    sys.stdout.write("\n")


def type_command(args: List[str]):
    if args[0] in COMMANDS:
        sys.stdout.write(f"{args[0]} is a shell builtin")
        sys.stdout.write("\n")
    elif args[0] == "cat":
        sys.stdout.write("cat is /bin/cat")
        sys.stdout.write("\n")
    else:
        sys.stdout.write(f"{args[0]} not found")
        sys.stdout.write("\n")


# mini shell
def main():
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

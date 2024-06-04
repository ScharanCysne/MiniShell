import sys


def main():
    # List of valid commands
    commands = ["ls", "echo", "mkdir", "exit"]

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
        if command not in commands:
            sys.stdout.write(f"{command}: command not found\n")

        # Check for exit command
        if command.startswith("exit") and args and args[0] == "0":
            return


if __name__ == "__main__":
    main()

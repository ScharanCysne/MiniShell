import sys


def main():
    # List of valid commands
    commands = ["ls", "echo", "mkdir"]

    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    command = input()

    if command not in commands:
        sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()

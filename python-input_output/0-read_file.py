#!/usr/bin/python3
def read_file(filename=""):
    """Reads a UTF-8 text file and prints its content to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")  # end="" prevents extra newline


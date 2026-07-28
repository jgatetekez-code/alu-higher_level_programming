#!/usr/bin/python3
"""Module that contains a function to append text to a file."""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file and return the number of characters added."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)

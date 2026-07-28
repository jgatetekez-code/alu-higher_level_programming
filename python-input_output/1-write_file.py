#!/usr/bin/python3
"""Module for writing text to a file."""


def write_file(filename="", text=""):
    """Write text to a file and return characters written."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)

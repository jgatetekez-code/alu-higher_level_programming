#!/usr/bin/python3
"""Module that contains a function to read a text file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its contents."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")

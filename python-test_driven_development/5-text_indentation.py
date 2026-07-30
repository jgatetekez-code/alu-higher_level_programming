#!/usr/bin/python3
"""Module that defines the text_indentation function."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""

    for char in text:
        line += char

        if char in ".?:":
            print(line.strip())
            print()
            line = ""

    if line.strip():
        print(line.strip(), end="")

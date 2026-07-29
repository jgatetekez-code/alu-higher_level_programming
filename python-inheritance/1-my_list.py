#!/usr/bin/python3
"""Module containing a class that inherits from list."""


class MyList(list):
    """A class that extends the built-in list class."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))

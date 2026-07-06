#!/usr/bin/python3
"""Function that returns a list with all values multiplied by a number."""


def multiply_list_map(my_list=[], number=0):
    """Return new list with values multiplied by number."""
    return list(map(lambda x: x * number, my_list))

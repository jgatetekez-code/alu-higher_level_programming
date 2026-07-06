#!/usr/bin/python3
"""Function that returns a list with all values multiplied by a number."""


def multiply_list_map(my_list=[], number=0):
    """Return new list with all values multiplied by number using map."""
    return list(map(lambda x: x * number, my_list))

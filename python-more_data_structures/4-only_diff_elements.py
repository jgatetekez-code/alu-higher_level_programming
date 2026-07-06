#!/usr/bin/python3
"""Function that returns elements present in only one set."""


def only_diff_elements(set_1, set_2):
    """Return elements present in only one set.

    Args:
        set_1: first set
        set_2: second set

    Returns:
        Set of elements present in only one set
    """
    only_diff = set()

    for element in set_1:
        if element not in set_2:
            only_diff.add(element)

    for element in set_2:
        if element not in set_1:
            only_diff.add(element)

    return only_diff


if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Twitter", "Python"}
    result = only_diff_elements(set_1, set_2)
    print(result)

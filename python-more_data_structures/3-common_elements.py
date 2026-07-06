#!/usr/bin/python3
"""Function that returns common elements in two sets."""


def common_elements(set_1, set_2):
    """Return common elements between two sets.

    Args:
        set_1: first set
        set_2: second set

    Returns:
        Set of common elements
    """
    common = set()

    for element in set_1:
        if element in set_2:
            common.add(element)

    return common


if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Twitter", "Python"}
    result = common_elements(set_1, set_2)
    print(result)

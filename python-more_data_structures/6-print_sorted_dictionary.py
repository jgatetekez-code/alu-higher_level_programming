#!/usr/bin/python3
"""Function that prints a dictionary by ordered keys."""


def print_sorted_dictionary(a_dictionary):
    """Print dictionary by ordered keys.

    Args:
        a_dictionary: input dictionary

    Returns:
        Nothing - just prints
    """
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))


if __name__ == "__main__":
    a_dictionary = {
        "language": "C",
        "Number": 89,
        "track": "Software",
        "id": 12
    }
    print_sorted_dictionary(a_dictionary)

#!/usr/bin/python3
"""Function that returns the number of keys in a dictionary."""


def number_keys(a_dictionary):
    """Return number of keys in a dictionary.

    Args:
        a_dictionary: input dictionary

    Returns:
        Number of keys
    """
    return len(a_dictionary)


if __name__ == "__main__":
    a_dictionary = {"language": "C", "number": 13, "track": "Software"}
    result = number_keys(a_dictionary)
    print(result)

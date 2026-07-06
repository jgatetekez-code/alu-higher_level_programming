#!/usr/bin/python3
"""Function that replaces or adds key/value in a dictionary."""


def update_dictionary(a_dictionary, key, value):
    """Replace or add key/value in a dictionary.

    Args:
        a_dictionary: input dictionary
        key: key to update or add
        value: value to set

    Returns:
        Updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary


if __name__ == "__main__":
    a_dictionary = {"language": "C", "number": 13, "track": "Software"}

    # test 1 - replace existing key
    result = update_dictionary(a_dictionary, "language", "Python")
    print(result)

    # test 2 - add new key
    result = update_dictionary(a_dictionary, "city", "Kigali")
    print(result)

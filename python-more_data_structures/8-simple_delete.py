#!/usr/bin/python3
"""Function that deletes a key in a dictionary."""


def simple_delete(a_dictionary, key=""):
    """Delete a key in a dictionary.

    Args:
        a_dictionary: input dictionary
        key: key to delete

    Returns:
        Updated dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary


if __name__ == "__main__":
    a_dictionary = {"language": "C", "number": 13, "track": "Software"}

    # test 1 - delete existing key
    result = simple_delete(a_dictionary, "number")
    print(result)

    # test 2 - delete key that doesn't exist
    result = simple_delete(a_dictionary, "city")
    print(result)

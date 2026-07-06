#!/usr/bin/python3
"""Function that returns a new dictionary with all values multiplied by 2."""


def multiply_by_2(a_dictionary):
    """Return new dictionary with all values multiplied by 2.

    Args:
        a_dictionary: input dictionary

    Returns:
        New dictionary with values multiplied by 2
    """
    new_dictionary = {}

    for key in a_dictionary:
        new_dictionary[key] = a_dictionary[key] * 2

    return new_dictionary


if __name__ == "__main__":
    a_dictionary = {"John": 12, "Alex": 8, "Bob": 14, "Mike": 18}

    result = multiply_by_2(a_dictionary)
    print(result)
    print(a_dictionary)

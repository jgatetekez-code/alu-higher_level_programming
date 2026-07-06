#!/usr/bin/python3
"""Function that returns a key with the biggest integer value."""


def best_score(a_dictionary):
    """Return key with the biggest integer value.

    Args:
        a_dictionary: input dictionary

    Returns:
        Key with biggest value or None
    """
    if len(a_dictionary) == 0:
        return None

    best_key = None
    best_value = None

    for key in a_dictionary:
        if best_value is None or a_dictionary[key] > best_value:
            best_key = key
            best_value = a_dictionary[key]

    return best_key


if __name__ == "__main__":
    a_dictionary = {"John": 12, "Alex": 8, "Bob": 14, "Mike": 18}

    result = best_score(a_dictionary)
    print(result)

    # test empty dictionary
    result = best_score({})
    print(result)

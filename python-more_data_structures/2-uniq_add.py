#!/usr/bin/python3
"""Function that adds all unique integers in a list."""


def uniq_add(my_list=[]):
    """Add all unique integers in a list.

    Args:
        my_list: initial list of integers

    Returns:
        Sum of all unique integers
    """
    unique_numbers = []
    total = 0

    for number in my_list:
        if number not in unique_numbers:
            unique_numbers.append(number)
            total += number

    return total


if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print(result)

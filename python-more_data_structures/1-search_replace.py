#!/usr/bin/python3
"""Function that replaces all occurrences of an element in a list."""


def search_replace(my_list, search, replace):
    """Replace all occurrences of search with replace in a new list.

    Args:
        my_list: the initial list
        search: element to replace
        replace: new element

    Returns:
        New list with replaced values
    """
    new_list = []

    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)

    return new_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 3, 2, 1]
    search = 2
    replace = 89
    result = search_replace(my_list, search, replace)
    print(result)
    print(my_list)

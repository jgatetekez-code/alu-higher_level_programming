#!/usr/bin/python3
"""Module that defines the matrix_divided function."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with all elements divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a matrix of integers/floats.
        TypeError: If rows are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_size = None

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row]
            for row in matrix]

#!/usr/bin/python3
"""Function that computes the square value of all integers of a matrix."""


def square_matrix_simple(matrix=[]):
    """Compute square of each value in matrix.

    Args:
        matrix: 2 dimensional array

    Returns:
        New matrix with squared values
    """
    return [list(map(lambda x: x ** 2, row)) for row in matrix]

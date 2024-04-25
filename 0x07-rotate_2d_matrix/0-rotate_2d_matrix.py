#!/usr/bin/python3
"""This script contains a function that
rotates a 2D matrix 90 degrees clockwise,
in place
"""


def rotate_2d_matrix(matrix):
    """This function rotates a 2D matrix
    90 degrees clockwise, in place
    """
    n = len(matrix)  # Number of sides
    m = n - 1  # Max index value

    # Reverse all columns
    for c in range(n):  # Iterate through all columns
        for r in range(int(n / 2)):
            buffer = matrix[r][c]
            matrix[r][c] = matrix[m - r][c]
            matrix[m - r][c] = buffer

    # Transpose the matrix
    for r in range(n):
        for c in range(r + 1, n):
            buffer = matrix[r][c]
            matrix[r][c] = matrix[c][r]
            matrix[c][r] = buffer

#!/usr/bin/python3
"""This script contains a function that
generates a pascal triangle"""


def pascal_triangle(n):
    """returns a list of lists of initegers
    representing a Pascal's triangle of n
    """
    rows = []
    if n <= 0:
        return rows

    for i in range(n):
        # Check if it's the first row
        if i == 0:
            rows.append([1])
            continue

        # copy the contents of the previous row
        prev = rows[i - 1].copy()

        # Declare a container for the new row and append 1
        row = []
        row.append(1)

        # Loop through the contents of the previous row, adding up
        # the value at index and value at next index
        j = 0
        while j < i - 1:
            row.append(prev[j] + prev[j + 1])
            j += 1

        # Append 1 and add to list of rows
        row.append(1)
        rows.append(row)

    return rows

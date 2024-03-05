#!/usr/bin/python3
"""
pascal's triangle function
"""


def pascal_triangle(n):
    """
    pascal_triangle(n): returns a list of lists of integers representing
    the Pascal’s triangle of n
    Returns an empty list if n <= 0
    """
    if n <= 0:
        return []
    ps = [[1]]
    for h in range(1, n):
        row = [1]
        pre = ps[h - 1]
        for j in range(len(pre)):
            new = pre[j] + pre[j + 1] if j != len(pre) - 1 else 1
            row.append(new)
        ps.append(row)

    return ps

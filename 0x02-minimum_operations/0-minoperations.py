#!/usr/bin/python3
"""This script conntains a function that  calculates
the fewest number of operations needed to result in
exactly n H characters in a file
"""


def minOperations(n):
    """function that  calculates the fewest
    number of operations needed to result in
    exactly n H characters in a file
    """
    total: int = 1
    ops: int = 0
    current: int = 0

    if n <= 0:
        return ops

    while True:
        if total == 1:
            current = total
            total += current
            ops += 2
            continue
        if n % total == 0:
            current = total
            total += current
            ops += 2
        else:
            total += current
            ops += 1
        if n <= total:
            return ops

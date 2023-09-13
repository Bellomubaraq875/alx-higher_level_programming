#!/usr/bin/python3
"""task 12"""


def pascal_triangle(n):
    """this function returns a list kf lists of integers
    representing the triangle
    """
    if n <= 0:
        return []

    triad = [[1]]
    while len(triad) != n:
        meta = triad[-1]
        unp = [1]
        for index in range(len(meta) - 1):
            unp.append(meta[index] + meta[index + 1])
        unp.append(1)
        triad.append(unp)
    return triad

#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """create pascal triangle"""
    if n <= 0:
        return []
    pascal = [[1]]
    while (len(pascal) < n):
        row = [1]
        for i in range(1, len(pascal[-1])):
            row.append(pascal[-1][i - 1] + pascal[-1][i])
        row.append(1)
        pascal.append(row)
    return pascal

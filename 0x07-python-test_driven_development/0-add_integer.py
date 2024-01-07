#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """ Return the addition of a and b

    Cast float values to int

    Raises:
      TypeError: If a and b are not int or float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

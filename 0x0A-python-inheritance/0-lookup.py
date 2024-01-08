#!/usr/bin/python3
"""Define lookup function that"""


def lookup(obj):
    """lookup function
    Args:
        obj: class name
    Return: list of all attribute and methods of class
    """
    return dir(obj)

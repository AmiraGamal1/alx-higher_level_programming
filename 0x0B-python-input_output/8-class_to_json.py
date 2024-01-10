#!/usr/bin/python3
"""Defines class_to_json function"""


def class_to_json(obj):
    """serialize the object
    Args:
        obj: object
    Return: dictionary
    """
    return obj.__dict__

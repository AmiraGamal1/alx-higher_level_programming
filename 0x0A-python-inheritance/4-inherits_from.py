#!/usr/bin/python3
"""Define inherits_from function"""


def inherits_from(obj, a_class):
    """ inherits_from function
    Args:
        obj (object): object
        a_class: class name
    Return: Ture if obj is a_class False else
    """
    return  isinstance(obj, a_class)
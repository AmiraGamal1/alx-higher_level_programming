#!/usr/bin/python3

def safe_print_integer(value):
    """Print integer
    Args:
        value (int): the value to be print
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)

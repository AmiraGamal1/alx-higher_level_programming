#!/usr/bin/python3

def safe_print_division(a, b):
    """safe division

    Args:
         a (int): int value
         b (int): int value
    Returns:
         division result or None
    """
    try:
        res = a / b
    except (TypeError, ZeroDivisionError):
        res = None
    finally:
        print("Inside result: {}".format(res))
    return (res)

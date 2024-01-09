#!/usr/bin/python3
"""Define from json string"""


import json


def from_json_string(my_str):
    """convert json to python object
    Args:
        my_str: json string
    Return: python object
    """
    return json.loads(my_str)

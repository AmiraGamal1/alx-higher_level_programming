#!/usr/bin/python3
"""Define to_json_string"""


import json


def to_json_string(my_obj):
    """convert object to json
    Args:
        my_obj: object
    Return: json representaion"""
    return json.dumps(my_obj)

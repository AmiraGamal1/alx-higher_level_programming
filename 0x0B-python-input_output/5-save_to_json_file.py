#!/usr/bin/python3
"""Define save_to_json_file"""


import json


def save_to_json_file(my_obj, filename):
    """write json representaion to a file
    Args:
        my_obj: python object
        filename: file name
    Return: nothings
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)

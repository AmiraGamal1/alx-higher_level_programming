#!/usr/bin/python3
"""Define load_from_json_file"""
import json


def load_from_json_file(filename):
    """creates object from json
    Args:
        filename: utf-8 file
    Return: nothings
    """
    with open(filename) as file:
        return json.load(file)

#!/usr/bin/python3
"""Defines write_file"""


def write_file(filename="", text=""):
    """write to a file"""
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)

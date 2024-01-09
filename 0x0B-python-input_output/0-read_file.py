#!/usr/bin/python3
"""Defines a read_file function"""


def read_file(filename=""):
    """read from file
    Args:
        filename: utf-8 file
    Return: nothings
    """

    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end='')

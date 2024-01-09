#!/usr/bin/python3
"""Defines append_wirte function"""


def append_write(filename="", text=""):
    """append to a file
    Args:
        filename: utf-8 file
        text: text to append to a file
    Return: number of character added
    """

    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)

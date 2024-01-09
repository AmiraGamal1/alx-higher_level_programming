#!/usr/bin/python3
"""Defines a read_file function"""


def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end='')

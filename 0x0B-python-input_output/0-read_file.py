#!/usr/bin/python3
"""Defines a read_file function"""


def read_file(filename=""):
    with open(filename, 'r') as file:
        print(file.read(), end='')

#!/usr/bin/python3
"""Define MyList class"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        print(sorted(self))

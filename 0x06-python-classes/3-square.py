#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a Square"""
    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): size of square.
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the square area"""
        return (self.__size * self.__size)

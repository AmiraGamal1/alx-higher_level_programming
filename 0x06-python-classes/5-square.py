#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a Square"""
    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): size of square.
        """
        self.size = size

    @property
    def size(self):
        """get the size value"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter function"""
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the square area"""
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        for w in range(self.__size):
            for h in range(self.__size):
                print("#", end='')
            print("")

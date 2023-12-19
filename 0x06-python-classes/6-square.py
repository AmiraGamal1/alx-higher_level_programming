#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): size of square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """get position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """set position"""
        if (not type(value) is tuple or
           (len(value) != 2) or
           not all(isinstance(i, int) for i in value) or
           not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the square area"""
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        for w in range(self.__size):
            for p in range(self.__position[0]):
                print(" ", end="")
            for h in range(self.__size):
                print("#", end='')
            print("")

#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a Rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """instance of the class

        Args:
            width (int): The width
            height (int): The height
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width + 2 * self.__height)

    def __str__(self):
        squre = ""
        if self.__height == 0 or self.__width == 0:
            return ("")
        for i in range(self.__height):
            for j in range(self.__width):
                squre += "#"
            if i < self.__height - 1:
                squre += "\n"
        return (squre)

    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a Rectangle."""

    def __init__(self, width=0, height=0):
        """instance of the class

        Args:
        width (int): The width
        height (int): The height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.height
    
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
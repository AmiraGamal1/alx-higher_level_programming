#!/usr/bin/python3
"""rectangle using BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return (self.__height * self.__width)

    def __str__(self):
        s = "[" + str(self.__class__.__name__) + "]"
        s += " " + str(self.__width) + "/" + str(self.__height)
        return s

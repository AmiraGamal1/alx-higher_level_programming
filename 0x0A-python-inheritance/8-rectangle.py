#!/usr/bin/python3

class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """Raise error area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name, str))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name, str))


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

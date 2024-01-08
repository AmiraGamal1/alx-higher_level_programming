#!/usr/bin/python3
"""Define BaseGeometry class"""


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

#!/usr/bin/python3
"""Define Student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """initialize a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dictionary of class attribute"""
        if (isinstance(attrs, list) and
                all(isinstance(attrs[i], str) for i in range(len(attrs)))):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        return self.__dict__

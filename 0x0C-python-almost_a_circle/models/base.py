#!/usr/bin/python3
"""base class to manage instance id"""


class Base:
    """base class model
    Private class attribute: (int) __nb_objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        Args:
            id (int): the identity of the new instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

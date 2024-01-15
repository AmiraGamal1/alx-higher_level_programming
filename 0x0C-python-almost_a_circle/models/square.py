#!/usr/bin/python3
"""Define Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    "Define Square"
    def __init__(self, size, x=0, y=0, id=None):
        """new instance of Square
        Args:
            size (int): size of square
            x: int
            y: int
            id: int
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self._Rectangle__x, self._Rectangle__y,
                   self._Rectangle__width)

    @property
    def size(self):
        """return the size"""
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """set the size"""
        Rectangle.width.fset(self, value)
        Rectangle.height.fset(self, value)

    def update(self, *args, **kwargs):
        """update id, size, x, y"""
        if args and len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self._Rectangle__x = args[2]
                self._Rectangle__y = args[3]
            except IndexError:
                pass
        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                elif key == "size":
                    self._Rectangle__width = val
                    self._Rectangle__heigh = val
                elif key == "x":
                    self._Rectangle__x = val
                elif key == "y":
                    self._Rectangle__y = val
                else:
                    raise AttributeError

    def to_dictionary(self):
        """return the class attributes"""
        return {"id": self.id, "size": self._Rectangle__width,
                "x": self._Rectangle__x, "y": self._Rectangle__y}

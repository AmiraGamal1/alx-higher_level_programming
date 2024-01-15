#!/usr/bin/python3
"""Define Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Define new Rectangle
        Args:
            width (int): width >= 0
            height (int): height >= 0
            x (int): x > 0
            y (int): y > 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """return the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width if value > 0 and int"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """return the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height if value > 0 and int"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """return x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x if the value >= 0 and int"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """return y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y if value >= 0 and int"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """display the rectangle use #"""
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        [print("") for i in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for j in range(self.__x)]
            [print("#", end="") for j in range(self.__width)]
            print("")

    def __str__(self):
        """return [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update Rectangle attribute use args
        Args:
            args: arguments
            kwargs: key vlaue arguments
        """
        if len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        elif len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                elif key == "width":
                    self.__width = val
                elif key == "height":
                    self.__height = val
                elif key == "x":
                    self.__x = val
                elif key == "y":
                    self.__y = val
                else:
                    raise AttributeError

    def to_dictionary(self):
        """return Rectangle attribute and its value"""
        return {"x": self.__x, "y": self.__y,
                "id": self.id, "height": self.__height,
                "width": self.__width}

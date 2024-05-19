#!/usr/bin/python3
"""Module for Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """Class for Rectangle.

    Args:
        Base (parent_class)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle constructor.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif type(x) is not int:
            raise TypeError("x must be an integer")
        elif type(y) is not int:
            raise TypeError("y must be an integer")
        if type(id) is not int:
            raise TypeError("id must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        elif height <= 0:
            raise ValueError("height must be > 0")
        elif x < 0:
            raise ValueError("x must be >= 0")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """The getter.
        """
        return self.__width

    @property
    def height(self):
        """The getter.
        """
        return self.__height

    @property
    def x(self):
        """The getter.
        """
        return self.__x

    @property
    def y(self):
        """The getter.
        """
        return self.__y

    @width.setter
    def width(self, value):
        """The setter.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """The setter.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """The setter.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """The setter.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
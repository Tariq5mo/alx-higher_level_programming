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
        self.__width = value

    @height.setter
    def height(self, value):
        """The setter.
        """
        self.__height = value

    @x.setter
    def x(self, value):
        """The setter.
        """
        self.__x = value

    @y.setter
    def y(self, value):
        """The setter.
        """
        self.__y = value

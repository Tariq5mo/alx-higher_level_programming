#!/usr/bin/python3
"""This module for Rectangle class."""


class Rectangle:
    """
    Class that define a rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Constructor.

        Args:
        width: The width of rectangle.
        height: The height of rectangle.
        Raises:
        TypeError: If one of them is not integer.
        ValueError: if one of them is less than 0.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """
        Returns the rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the rectangle perimeter.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    @property
    def width(self):
        """To retrieve it."""
        return self.__width

    @property
    def height(self):
        """To retrieve it."""
        return self.__height

    @width.setter
    def width(self, value):
        """To set width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """To set height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """
        Return the rectangle with the character #
        """
        rec = ""
        for n in range(0, self.__height):
            for m in range(0, self.__width):
                rec = rec + str((self.print_symbol))
            if n < self.__height - 1:
                rec = rec + "\n"
        return rec

    def __repr__(self):
        """
        Return a string representation of the rectangle
        to be able to recreate a new instance by using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Delete an instance.
        """
        print("Bye rectangle...")
        if (Rectangle.number_of_instances > 0):
            Rectangle.number_of_instances -= 1
        del self

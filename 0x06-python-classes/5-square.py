#!/usr/bin/python3
"""module for Square class"""


class Square:
    """Class that define a square."""

    def __init__(self, size=0):
        """
        Constructor.

        Args:
        size: The size of square.
        Raises:
        TypeError: If size is not integer.
        ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """The getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """The setter of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area.
        Returns:
        The square of size
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints in stdout the square with the character #

        if size is 0, prints empty line
        """
        if self.__size == 0:
            print()
            return
        for i in range(0, self.__size):
            for i in range(0, self.__size):
                print("#", end="")
            print()

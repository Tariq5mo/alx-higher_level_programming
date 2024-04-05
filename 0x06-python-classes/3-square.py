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

    def area(self):
        """
        Returns the current square area.
        Returns:
        The square of size
        """
        return self.__size ** 2

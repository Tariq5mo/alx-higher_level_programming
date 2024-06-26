#!/usr/bin/python3
"""module for Square class"""


class Square:
    """Class that define a square."""

    def __init__(self, size=0):
        """
        Constructor.

        Args:
        size: the size of square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

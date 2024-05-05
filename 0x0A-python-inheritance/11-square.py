#!/usr/bin/python3
'''Task 10.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define a square."""

    def __init__(self, size):
        """
        size must be private. No getter or setter
        size must be a positive integer, validated by integer_validator.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''Return the area of square.'''
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

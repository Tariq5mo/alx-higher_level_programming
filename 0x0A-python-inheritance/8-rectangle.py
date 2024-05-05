#!/usr/bin/python3
'''Task 8.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    Class for rectangle.
    '''
    def __init__(self, width, height):
        '''
        Instantiation rectangle with width and height.
        '''
        # integer_validator = super().integer_validator
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

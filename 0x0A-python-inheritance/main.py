#!/usr/bin/python3
'''Task 8.'''


class BaseGeometry:
    '''
    Base class.
    '''
    def __init__(self, name, age):
        '''init'''
        self.n = name
        self.ag = age

    def area(self):
        '''
        Raises an Exception with the message area() is not implemented.
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Validates value.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less or equal to 0.
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(str(name)))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(str(name)))


class Rectangle(BaseGeometry):
    '''
    Class for rectangle.
    '''
    def __init__(self, width, height):
        '''
        Instantiation rectangle with width and height.
        '''
        self.a = BaseGeometry.integer_validator
        self.b = self.integer_validator
        self.c = super().integer_validator


cl = Rectangle(15, 16)
cl.c('good', '78')
cl.b()


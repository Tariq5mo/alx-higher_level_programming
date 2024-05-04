#!/usr/bin/python3
'''Task 5.'''


class BaseGeometry:
    '''
    Base class.
    '''
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


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")

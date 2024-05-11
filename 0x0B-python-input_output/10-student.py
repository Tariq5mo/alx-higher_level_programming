#!/usr/bin/python3
"""Module for Student class
"""


class Student:
    """Defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """Instantiation the instance.

        Args:
            first_name (str)
            last_name (str)
            age (int)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings,
        only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved.

        Returns:
            Dictionary: Dictionary representation of a Student instance.
        """
        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
            d = {}
            for i in attrs:
                if i in self.__dict__:
                    d[i] = self.__dict__.get(i)
            return d
        return self.__dict__

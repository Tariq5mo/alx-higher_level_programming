#!/usr/bin/python3
"""Module for class Base.
"""


class Base:
    """This class will be the “base” of all other classes in this project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor.

        Args:
            id (int): The id of the instance. Defaults to None.
        """
        if type(id) is not int and id is not None:
            raise TypeError("id must be an integer")
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

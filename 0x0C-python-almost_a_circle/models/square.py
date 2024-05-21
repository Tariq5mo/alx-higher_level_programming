#!/usr/bin/python3
"""Module for class Square.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class for Square that inherits from Rectangle.

    Args:
        Rectangle (class): The class that Square inherits from it.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """

        Args:
            size (int): The size of square.
            x (int, optional): x of x axis. Defaults to 0.
            y (int, optional): y of y axis. Defaults to 0.
            id (int, optional): the id of square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """Getter for size of square.
        """
        # return self.size
        return self.width

    @size.setter
    def size(self, value):
        """Setter of size.

        Args:
            value (int): The length of the rib.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes.
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) == 4:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary representation of a Square.
        """
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}

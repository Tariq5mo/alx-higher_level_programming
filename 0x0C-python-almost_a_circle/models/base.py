#!/usr/bin/python3
"""Module for class Base.
"""
import json
import models.rectangle
import models.square


class Base:
    """This class will be the “base” of all other classes in this project.
    """
    __nb_objects = 0

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Returns:
            an instance of class.
        """
        if 'width' in dictionary:
            dummy = Rectangle(10, 10)
        else:
            dummy = Square(10)
        dummy.update(dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances who inherits of Base.
        """
        li = list(list_objs)
        ll = []
        for obj in li:  # put the dictionaries of instances in a list
            if isinstance(obj, Base) is False:
                return
            ll.append(obj.__dict__)
        json_list = cls.to_json_string(ll)
        json_list = json_list.replace(f"_{obj.__class__.__name__}__", '')
        with open(f"{obj.__class__.__name__}.json",
                  'w', encoding='utf-8') as f:
            f.write(json_list)

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

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.

        Args:
            json_string (str)

        Returns:
            list: Return the list represented by json_string.
        """
        if json_string is None or json_string == '':
            return []
        return list(json.loads(json_string))

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list of dictionaries)
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

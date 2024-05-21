#!/usr/bin/python3
"""Module for class Base.
"""
import json


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
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy = Rectangle(10, 10)
        elif cls is Square:
            dummy = Square(10)
        else:
            dummy = None
            return
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances who inherits of Base.
        """
        ll = []
        if list_objs is None or list_objs == []:
            with open(f"{cls.__name__}.json", 'w', encoding='utf-8') as f:
                f.write(json.dumps([]))
        else:
            for obj in list_objs:  # put the dictionaries of instances in list
                if isinstance(obj, Base) is False:
                    return
                ll.append(obj.to_dictionary())
        json_list = cls.to_json_string(ll)
        json_list = json_list.replace(f"_{cls.__name__}__", '')
        with open(f"{cls.__name__}.json",
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
            return "[]"
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

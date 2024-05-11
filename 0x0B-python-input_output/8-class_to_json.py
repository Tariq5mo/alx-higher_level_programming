#!/usr/bin/python3
"""Module for a function that returns the dictionary description.
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.

    Args:
        obj : An instance of a Class

    Returns:
        dictionary: dictionary description with simple data structure
    (list, dictionary, string, integer and boolean).
    """
    return obj.__dict__

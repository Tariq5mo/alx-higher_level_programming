#!/usr/bin/python3
"""
Task 4.
"""


import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.
    Args:
        my_str (str): JSON string

    Returns:
        object: An object (Python data structure).
    """
    return json.loads(my_str)

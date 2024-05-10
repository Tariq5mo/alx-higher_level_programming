#!/usr/bin/python3
'''Task 3.'''

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    Args:
        my_obj (anytype): An object to JSON representation.

    Returns:
        Returns the JSON representation.
    """
    return json.dumps(my_obj)

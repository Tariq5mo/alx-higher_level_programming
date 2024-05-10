#!/usr/bin/python3
"""
    Task 5.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.
    Args:
        my_obj (any_type): The object which convert json.
        filename (str): The file which write the text into.
    """    
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))

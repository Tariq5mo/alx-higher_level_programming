#!/usr/bin/python3
"""
    Task 6. module for function that creates an Object from a “JSON file”.
"""


import json
from os import read


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”.
    Args:
        filename : JSON file.
    """
    with open(filename, 'r') as f:
        return json.load(f)

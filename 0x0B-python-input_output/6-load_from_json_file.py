#!/usr/bin/python3
"""
    Task 6. module for function that creates an Object from a “JSON file”.
"""


import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”.
    Args:
        filename : JSON file.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)

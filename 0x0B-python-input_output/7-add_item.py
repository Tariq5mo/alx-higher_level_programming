#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then save them to a file.
The list saved as a JSON representation in a file named add_item.json.
"""
import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

try:
    l1 = list(load_from_json_file('add_item.json'))
except FileNotFoundError:
    save_to_json_file([], 'add_item.json')
    exit()
l2 = sys.argv
l1.extend(l2[1:])
save_to_json_file(l1, "add_item.json")

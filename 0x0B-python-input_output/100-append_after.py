#!/usr/bin/python3
"""Module for task 100.
"""


def append_after(filename="", search_string="", new_string=""):
    """Append a str aftr a line in a file.

    Args:
        filename (str, optional): The name of the file. Defaults to "".
        search_string (str, optional): String which search. Defaults to "".
        new_string (str, optional): The string which include. Defaults to "".
    """
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if line == "":
                break
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(''.join(lines))

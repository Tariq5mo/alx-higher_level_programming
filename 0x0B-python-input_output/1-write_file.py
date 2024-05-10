#!/usr/bin/python3
'''Task 1.'''


def write_file(filename="", text=""):
    '''
    Writes a string to a text file (UTF8),
    and returns the number of characters written.
    '''
    with open(filename, mode='w', encoding="utf-8", newline='\r\n') as f:
        return f.write(str(text))

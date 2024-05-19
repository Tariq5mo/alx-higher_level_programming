#!/usr/bin/python3
'''Task 0.'''


def read_file(filename=""):
    '''
    reads a text file (UTF8) and prints it to stdout.
    '''
    with open(filename, encoding="utf8") as f:
        print(f.read(), end='')

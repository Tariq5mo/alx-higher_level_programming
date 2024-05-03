#!/usr/bin/python3
'''For task 2'''


def is_same_class(obj, a_class):
    '''
    Returns True if the obj is an instance of a_class class ; otherwise False.
    '''
    if type(obj) is a_class:
        return True
    else:
        return False

#!/usr/bin/python3
'''Task 10.'''


class MyInt(int):
    '''Rebel the int. MyInt has == and != operators inverted.'''

    def __init__(self, value):
        '''return'''
        self.value = value

    def __eq__(self, other):
        return self.value != other

    def __ne__(self, other):
        return self.value == other

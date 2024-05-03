#!/usr/bin/python3
'''Try.'''


class MyList(list):
    '''Inherits from list.'''

    def print_sorted(self):
        '''
        Prints the list, but sorted (ascending sort).
        '''
        for i in range(0, len(self)):
            self[i] = int(self[i])
        return sorted(self.copy())


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")

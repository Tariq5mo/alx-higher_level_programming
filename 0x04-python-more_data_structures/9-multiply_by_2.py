#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    di = dict(a_dictionary)
    for i in di:
        di[i] = int(di[i]) * 2
    return di

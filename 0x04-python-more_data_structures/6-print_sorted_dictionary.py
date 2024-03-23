#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    di = dict(a_dictionary)
    order_di = sorted(di)
    for key in order_di:
        print("{}: {}".format(str(key), di[key]))

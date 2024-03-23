#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list == []:  # check if it's empty
        return 0
    for i in range(0, len(my_list)):  # convert each object to int
        my_list[i] = int(my_list[i])
    m = set(my_list)  # to be unique
    sum = 0
    for n in m:
        sum = sum + n
    return sum

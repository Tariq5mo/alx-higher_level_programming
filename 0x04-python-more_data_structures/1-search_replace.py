#!/usr/bin/python3
def search_replace(my_list, search, replace):
    li = list(my_list.copy())
    for i in range(0, len(li)):
        if li[i] == search:
            li[i] = replace
    return li

#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list) or my_list == []:
        return None
    my_list[idx] = element
    return my_list

#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if not my_list:
        return None
    if idx < 0 or idx >= len(my_list) or my_list == []:
        return my_list
    copy_list = my_list.copy()
    copy_list[idx] = element
    return copy_list

#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) or my_list == []:
        return None
    return int(my_list[idx])

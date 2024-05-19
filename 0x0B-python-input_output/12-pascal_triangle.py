#!/usr/bin/python3
"""Module for pascal_triangle function.
"""


def pascal_triangle(n):
    """Make list of lists of integers representing the Pascal's triangle of n.

    Args:
        n (int): Integer representing the Pascal's triangle.

    Returns:
        list: Returns a list of lists of integers.
    """
    num = int(n)
    if num <= 0:
        return []
    list_lists = []
    for i in range(1, num + 1):
        built_list = [1]
        last_idx = i - 1
        j = 1
        while j < last_idx:
            built_list.append(prev_list[j - 1] + prev_list[j])
            j += 1
        if i != 1:
            built_list.append(1)
        prev_list = built_list
        list_lists.append(built_list)
    return list_lists

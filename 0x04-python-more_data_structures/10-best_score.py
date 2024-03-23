#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    dic = dict(a_dictionary)
    i = 0
    for check in dic:
        if dic[check] is not None:
            i = 1
            break
    if i == 0:
        return None
    k = check
    for key in dic:
        if dic[key] is not None:
            if dic[key] > dic[k]:
                k = key
    return k

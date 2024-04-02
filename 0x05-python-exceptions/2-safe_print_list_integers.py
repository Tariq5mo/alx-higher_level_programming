#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if my_list is None or x is None:
        return 0
    i, n = 0, 0
    rx = int(x)
    rlist = list(my_list)
    while (i < rx):
        try:
            print("{:d}".format(rlist[i]), end="")
            n = n + 1
            i = i + 1
        except (ValueError, TypeError):
            i = i + 1
    print("")
    return n

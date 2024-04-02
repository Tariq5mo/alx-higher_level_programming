#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    i = 0
    rx = int(x)
    rlist = list(my_list)
    while (i < rx):
        try:
            print("{:d}".format(int(rlist[i])), end="")
            n = n + 1
            i = i + 1
        except ValueError:
            i = i + 1
        except IndexError:
            print("")
            return n
    print("")
    return n

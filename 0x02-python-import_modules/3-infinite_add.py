#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = argv[1:]
    i = 0
    for arg in args:
        i += int(arg)
    print(i)

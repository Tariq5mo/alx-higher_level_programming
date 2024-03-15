#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(argv) - 1))
    args = argv[1:]
    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))

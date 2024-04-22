#!/usr/bin/python3
def magic_string():
    magic_string.var = getattr(magic_string, "var", 0) + 1
    return ", ".join(["BestSchool" for i in range(0, magic_string.var)])

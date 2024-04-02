#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = float(int(a) / int(b))
    except (ZeroDivisionError, ValueError, ArithmeticError, TypeError):
        c = None
    finally:
        if c is not None:
            print("Inside result: {:.1f}".format(c))
        else:
            print("Inside result: None")
        return c

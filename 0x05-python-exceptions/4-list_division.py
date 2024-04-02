#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_1 = list(my_list_1)
    my_list_2 = list(my_list_2)
    list_length = int(list_length)
    i = 0
    n = []
    while i < list_length:
        try:
            n.append(my_list_1[i]/my_list_2[i])
        except (TypeError, ValueError):
            print("wrong type")
            n.append(0)
        except (ZeroDivisionError, ArithmeticError):
            print("division by 0")
            n.append(0)
        except IndexError:
            print("out of range")
            n.append(0)
        finally:
            i += 1
    return n

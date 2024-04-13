#!/usr/bin/python3
"""
module for task 1
Functions:
matrix_divided()
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    """
    E = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    elif type(matrix) is not list or matrix == []:
        raise TypeError(E)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    s = len(matrix[0])
    for i in range(0, len(matrix)):
        if len(matrix[i]) != s:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(0, len(matrix[i])):
            if type(matrix[i][j]) not in (int, float):
                raise TypeError(E)
    m = matrix.copy()
    for i in range(0, len(matrix)):
        m[i] = matrix[i].copy()
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            m[i][j] = round(m[i][j] / div, 2)
    return m

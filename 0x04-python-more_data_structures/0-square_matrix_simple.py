#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = matrix.copy()  # copy the the array of pointers
    for i in range(0, len(m)):  # copy lists in matrix
        m[i] = matrix[i].copy()
    for i in m:
        for j in range(0, len(i)):
            i[j] = i[j] ** 2
    return m

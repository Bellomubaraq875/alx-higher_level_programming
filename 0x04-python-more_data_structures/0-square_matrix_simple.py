#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for row in matrix:
        newRow = list(map((lambda x: x**2), row))
        newMatrix.append(newRow)
    return newMatrix

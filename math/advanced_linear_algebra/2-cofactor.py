#!/usr/bin/env python3
"""Module to calculate the cofactor matrix of a matrix."""


def determinant(matrix):
    """Calculate the determinant of a square matrix."""
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for j in range(len(matrix)):
        sub = [row[:j] + row[j + 1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(sub)
    return det


def cofactor(matrix):
    """Calculate the cofactor matrix of a matrix."""
    if type(matrix) is not list or len(matrix) == 0 or \
            not all(type(row) is list for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if len(matrix) != len(matrix[0]) or \
            not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) == 1:
        return [[1]]
    cofactors = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            sub = [r[:j] + r[j + 1:]
                   for r in (matrix[:i] + matrix[i + 1:])]
            row.append(((-1) ** (i + j)) * determinant(sub))
        cofactors.append(row)
    return cofactors

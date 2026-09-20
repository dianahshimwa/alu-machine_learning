#!/usr/bin/env python3
"""Module to calculate the determinant of a matrix."""


def determinant(matrix):
    """Calculate the determinant of a matrix."""
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    if not all(type(row) is list for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if matrix == [[]]:
        return 1
    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for j in range(len(matrix)):
        sub = [row[:j] + row[j + 1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(sub)
    return det

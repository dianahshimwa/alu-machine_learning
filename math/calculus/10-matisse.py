#!/usr/bin/env python3
"""Module to calculate the derivative of a polynomial."""


def poly_derivative(poly):
    """Return the derivative of a polynomial as a list of coefficients."""
    if type(poly) is not list or len(poly) == 0:
        return None
    if not all(isinstance(c, (int, float)) for c in poly):
        return None
    if len(poly) == 1:
        return [0]
    derivative = [poly[i] * i for i in range(1, len(poly))]
    if all(c == 0 for c in derivative):
        return [0]
    return derivative

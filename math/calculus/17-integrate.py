#!/usr/bin/env python3
"""Module to calculate the integral of a polynomial."""


def poly_integral(poly, C=0):
    """Return the integral of a polynomial as a list of coefficients."""
    if type(poly) is not list or len(poly) == 0:
        return None
    if not all(isinstance(c, (int, float)) for c in poly):
        return None
    if not isinstance(C, (int, float)):
        return None
    integral = [C]
    for i in range(len(poly)):
        coef = poly[i] / (i + 1)
        if coef == int(coef):
            coef = int(coef)
        integral.append(coef)
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()
    return integral

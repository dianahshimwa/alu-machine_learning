#!/usr/bin/env python3
"""Module to calculate the summation of i squared from 1 to n."""


def summation_i_squared(n):
    """Return the sum of i^2 for i from 1 to n, or None if invalid."""
    if type(n) is not int or n < 1:
        return None
    return n * (n + 1) * (2 * n + 1) // 6

#!/usr/bin/env python3
"""Module to concatenate two numpy arrays along an axis."""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenate two numpy arrays along a given axis as a new array."""
    return np.concatenate((mat1, mat2), axis=axis)

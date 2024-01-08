#!/usr/bin/python3
"""This defines a matrix multiplication function using NumPy library!"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """To return the multiplication!

    Args:
        m_a (list of lists of ints/floats): Is the first matrix
        m_b (list of lists of ints/floats): Is the second matrix
    """

    return (np.matmul(m_a, m_b))

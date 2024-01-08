#!/usr/bin/python3
"""This defines a matrix multiplication function!"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): Is the first matrix (MxN).
        m_b (list of lists of ints/floats): Is the second matrix (NxP).

    Raises:
        ValueError: If matrices cannot be multiplied or matrices are empty.
        TypeError: If matrices contain non-numeric elements.

    Returns:
        list of lists: Resulting matrix (MxP).
    """
    if m_a == [] or m_a == [[]] or m_b == [] or m_b == [[]]:
        raise ValueError("Matrices cannot be empty")

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Matrices must be lists")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("Matrices must be lists of lists")

    if any(not all(isinstance(num, (int, float)) for num in row) for row in m_a + m_b):
        raise TypeError("Matrices should contain only integers or floats")

    rows_a, cols_a = len(m_a), len(m_a[0])
    rows_b, cols_b = len(m_b), len(m_b[0])

    if cols_a != rows_b:
        raise ValueError("Matrices cannot be multiplied")

    inverted_b = []
    for r in range(cols_b):
        new_row = []
        for c in range(rows_b):
            new_row.append(m_b[c][r])
        inverted_b.append(new_row)

    result = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = sum(a * b for a, b in zip(row, col))
            new_row.append(prod)
        result.append(new_row)

    return result

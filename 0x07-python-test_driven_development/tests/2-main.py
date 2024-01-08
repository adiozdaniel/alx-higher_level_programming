#!/usr/bin/python3
import importlib.util

spec = importlib.util.spec_from_file_location("matrix_divided", "../2-matrix_divided.py")
matrix_divided_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(matrix_divided_module)
matrix_divided = matrix_divided_module.matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

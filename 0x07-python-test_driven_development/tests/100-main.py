#!/usr/bin/python3
import importlib.util

spec = importlib.util.spec_from_file_location("matrix_mul", "../100-matrix_mul.py")
matrix_mul_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(matrix_mul_module)
matrix_mul = matrix_mul_module.matrix_mul

# Test cases
print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

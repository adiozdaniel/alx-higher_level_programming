#!/usr/bin/python3
import importlib.util

spec = importlib.util.spec_from_file_location("lazy_matrix_mul", "../101-lazy_matrix_mul.py")
lazy_matrix_mul_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lazy_matrix_mul_module)
lazy_matrix_mul = lazy_matrix_mul_module.lazy_matrix_mul

# Test cases
print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

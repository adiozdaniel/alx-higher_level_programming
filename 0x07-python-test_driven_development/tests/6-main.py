#!/usr/bin/python3
import importlib.util

spec = importlib.util.spec_from_file_location("max_integer", "../6-max_integer.py")
max_integer_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(max_integer_module)
max_integer = max_integer_module.max_integer

# Test cases
print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))


print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))

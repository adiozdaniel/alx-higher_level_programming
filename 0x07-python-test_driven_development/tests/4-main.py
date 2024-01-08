#!/usr/bin/python3
import importlib.util

spec = importlib.util.spec_from_file_location("print_square", "../4-print_square.py")
print_square_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(print_square_module)
print_square = print_square_module.print_square

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")

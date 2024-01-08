#!/usr/bin/python3
import importlib.util

spec = importlib.util.spec_from_file_location("add_integer", "../0-add_integer.py")
add_integer_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(add_integer_module)
add_integer = add_integer_module.add_integer


print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

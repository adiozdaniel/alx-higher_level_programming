#!/usr/bin/python3
import importlib.util

# Get MyInt from the main directory
spec = importlib.util.spec_from_file_location("my_int", "../100-my_int.py")
my_int_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(my_int_module)
MyInt = my_int_module.MyInt

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)

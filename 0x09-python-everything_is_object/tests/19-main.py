#!/usr/bin/python3
import importlib.util

spec = importlib.util.spec_from_file_location("copy_list", "../19-copy_list.py")
copy_list = importlib.util.module_from_spec(spec)
spec.loader.exec_module(copy_list)

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list.copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

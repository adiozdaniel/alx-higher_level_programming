#!/usr/bin/python3

import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
lister = ['hello', 'World']
lib.print_python_list_info(lister)
del lister[1]
lib.print_python_list_info(lister)
lister = lister + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(lister)
lister = []
lib.print_python_list_info(lister)
lister.append(0)
lib.print_python_list_info(lister)
lister.append(1)
lister.append(2)
lister.append(3)
lister.append(4)
lib.print_python_list_info(lister)
lister.pop()
lib.print_python_list_info(lister)

#!/usr/bin/python3
import ctypes

lib = ctypes.CDLL('./libPythonHBTN.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
l = []
lib.print_python_list(l)
l.append(0)
lib.print_python_list(l)
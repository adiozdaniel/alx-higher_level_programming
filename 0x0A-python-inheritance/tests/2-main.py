#!/usr/bin/python3
import importlib.util

# Get is_same_class from the main directory
spec = importlib.util.spec_from_file_location("is_same_class", "../2-is_same_class.py")
is_same_class_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(is_same_class_module)
is_same_class = is_same_class_module.is_same_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))

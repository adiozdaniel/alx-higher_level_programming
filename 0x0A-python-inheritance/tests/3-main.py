#!/usr/bin/python3
import importlib.util

# Get is_kind_of_class from the main directory
spec = importlib.util.spec_from_file_location("is_kind_of_class", "../3-is_kind_of_class.py")
is_kind_of_class_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(is_kind_of_class_module)
is_kind_of_class = is_kind_of_class_module.is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))

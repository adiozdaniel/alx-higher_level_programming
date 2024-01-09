#!/usr/bin/python3
import importlib.util

# Get inherits_from from the main directory
spec = importlib.util.spec_from_file_location("inherits_from", "../4-inherits_from.py")
inherits_from_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(inherits_from_module)
inherits_from = inherits_from_module.inherits_from

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))

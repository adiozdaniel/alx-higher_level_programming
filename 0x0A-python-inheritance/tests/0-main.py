#!/usr/bin/python3
import importlib.util

# Get lookup from the main directory
spec = importlib.util.spec_from_file_location("lookup", "../0-lookup.py")
lookup_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lookup_module)
lookup = lookup_module.lookup


class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))

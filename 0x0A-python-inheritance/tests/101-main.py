#!/usr/bin/python3
import importlib.util

# Get add_attribute from the main directory
spec = importlib.util.spec_from_file_location("add_attribute", "../101-add_attribute.py")
add_attribute_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(add_attribute_module)
add_attribute = add_attribute_module.add_attribute

class MyClass():
    pass

mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

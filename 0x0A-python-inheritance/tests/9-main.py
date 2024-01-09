#!/usr/bin/python3
import importlib.util

# Get Rectangle from the main directory
spec = importlib.util.spec_from_file_location("rectangle", "../9-rectangle.py")
rectangle_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rectangle_module)
Rectangle = rectangle_module.Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())

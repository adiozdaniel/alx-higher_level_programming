#!/usr/bin/python3
import importlib.util

# Get Rectangle from the main directory
spec = importlib.util.spec_from_file_location("rectangle", "../8-rectangle.py")
rectangle_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rectangle_module)
Rectangle = rectangle_module.Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

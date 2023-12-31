#!/usr/bin/python3
import importlib.util

# Get BaseGeometry from the main directory
spec = importlib.util.spec_from_file_location("base_geometry", "../7-base_geometry.py")
base_geometry_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base_geometry_module)
BaseGeometry = base_geometry_module.BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

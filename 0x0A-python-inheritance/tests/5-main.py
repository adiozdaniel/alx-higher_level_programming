#!/usr/bin/python3
import importlib.util

# Get BaseGeometry from the main directory
spec = importlib.util.spec_from_file_location("base_geometry", "../5-base_geometry.py")
base_geometry_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base_geometry_module)
BaseGeometry = base_geometry_module.BaseGeometry

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))

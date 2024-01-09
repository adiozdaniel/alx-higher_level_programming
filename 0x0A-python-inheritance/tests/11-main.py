#!/usr/bin/python3
import importlib.util

# Get Square from the main directory
spec = importlib.util.spec_from_file_location("square", "../11-square.py")
square_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(square_module)
Square = square_module.Square

s = Square(13)

print(s)
print(s.area())

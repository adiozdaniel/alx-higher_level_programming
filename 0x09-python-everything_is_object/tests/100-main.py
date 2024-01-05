#!/usr/bin/python3
import importlib.util

spec = importlib.util.spec_from_file_location("magic_string", "../100-magic_string.py")
magic_string = importlib.util.module_from_spec(spec)
spec.loader.exec_module(magic_string)

for i in range(10):
    print(magic_string.magic_string())

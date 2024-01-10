#!/usr/bin/python3
import importlib.util

# Get read_file from the main directory
spec = importlib.util.spec_from_file_location("read_file", "../0-read_file.py")
read_file_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(read_file_module)
read_file = read_file_module.read_file

read_file("my_file_0.txt")

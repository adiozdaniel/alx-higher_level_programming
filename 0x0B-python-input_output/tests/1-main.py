#!/usr/bin/python3
import importlib.util

# Get write_file from the main directory
spec = importlib.util.spec_from_file_location("write_file", "../1-write_file.py")
write_file_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(write_file_module)
write_file = write_file_module.write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)

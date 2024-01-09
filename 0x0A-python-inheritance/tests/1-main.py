#!/usr/bin/python3
import importlib.util

# Get MyList from the main directory
spec = importlib.util.spec_from_file_location("my_list", "../1-my_list.py")
my_list_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(my_list_module)
MyList = my_list_module.MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)

#!/usr/bin/python3
import importlib.util

spec = importlib.util.spec_from_file_location("LockedClass", "../101-locked_class.py")
LockedClass = importlib.util.module_from_spec(spec)
spec.loader.exec_module(LockedClass)

lc = LockedClass.LockedClass()  # Create an instance of the LockedClass
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

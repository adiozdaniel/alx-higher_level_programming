#!/usr/bin/python3
import importlib.util

spec = importlib.util.spec_from_file_location("say_my_name", "../3-say_my_name.py")
say_my_name_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(say_my_name_module)
say_my_name = say_my_name_module.say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)

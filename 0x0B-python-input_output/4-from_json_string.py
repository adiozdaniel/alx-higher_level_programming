#!/usr/bin/python3
"""This defines a JSON-to-object function!"""
import json


def from_json_string(my_str):
    """to return a Python object representation of a JSON string"""
    return json.loads(my_str)

#!/usr/bin/python3
""" Returns the string "BestSchool" n times the number given"""


def magic_string():
    """
    Returns a string "BestSchool" based on the current value of the counter!
    The counter increments with every iteration

    Returns:
        str: Concatenated string
    """
    if not hasattr(magic_string, "counter"):
        magic_string.counter = 1
    result = "BestSchool" * magic_string.counter
    magic_string.counter += 1
    return result

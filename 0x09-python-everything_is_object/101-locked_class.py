#!/usr/bin/python3
"""This class overrides the __setattr__ method"""


class LockedClass:
    """prevents creation of a new instance except for first_name"""
    __slots__ = ["first_name"]

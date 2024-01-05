#!/usr/bin/python3
"""
  This class overrides the __setattr__ method
  to prevent the creation of new instance attributes
  with an exception given for first_name.
"""


class LockedClass:
    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        super().__setattr__(name, value)

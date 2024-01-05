#!/usr/bin/python3
"""This class overrides the __setattr__ method"""


class LockedClass:
    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'"
                .format(name)
            )
        super().__setattr__(name, value)

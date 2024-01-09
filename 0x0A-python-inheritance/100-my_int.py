#!/usr/bin/python3
"""This defines a class MyInt that inherits from int!"""


class MyInt(int):
    """The Invert int operators == and !="""

    def __eq__(self, value):
        """Overrides == opeartor with != behavior!"""
        return self.real != value

    def __ne__(self, value):
        """Overrides != operator with == behavior!"""
        return self.real == value

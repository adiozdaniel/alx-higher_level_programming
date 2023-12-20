#!/usr/bin/python3
"""A MagicClass matching the given bytecode
  See Readme for more information
"""


import math


class MagicClass:

    def __init__(self, radius=0):
        """Initialize the MagicClass.

        Arg:
            radius (float or int): The radius of the new MagicClass class.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("the radius must be a number")
        self.__radius = radius

    def area(self):
        """This returns the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """This then returns a circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)

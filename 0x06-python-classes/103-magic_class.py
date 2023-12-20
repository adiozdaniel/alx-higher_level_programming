#!/usr/bin/python3
# Author: Adioz Daniel
"""The MagicClass definition"""
import math


class MagicClass:
    """Define a MagicClass for magical calculations"""

    def __init__(self, radius=0):
        """
        Initialize a MagicClass
        With two Args:
            radius (int or float): The radius of the magic.
        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the magic
        Returns:
            float: Te calculated area.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of the magic.
        Returns:
            float: The calculated circumfrance
        """
        return 2 * math.pi * self.__radius

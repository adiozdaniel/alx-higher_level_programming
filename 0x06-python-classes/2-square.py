#!/usr/bin/python3
"""class Square that definitions"""

class Square():
    """square class with it's size and validations"""

    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("the size must be an integer")
        elif (size < 0):
            raise ValueError("the size must be >= 0")
        self.__size = size

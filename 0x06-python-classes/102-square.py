#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args are the size (int) of the square
        """
        self.size = size

    @property
    def size(self):
        """Get or set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Instance == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Instance != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Instance < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Instance <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Instance > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Instance >= comparison to a Square."""
        return self.area() >= other.area()

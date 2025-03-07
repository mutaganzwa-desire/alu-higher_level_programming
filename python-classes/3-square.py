#!/usr/bin/python3

"""
This module defines a class called Square. The class has a private
instance attribute `size` and a public instance method `area` to
calculate the area of the square. The `size` must be an integer
and greater than or equal to 0.
"""


class Square:
    """
    A class that represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2

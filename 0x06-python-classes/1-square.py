#!/usr/bin/python3
"""
Module - Square
"""


class Square:
    """
    Defines a square with a private instance attribute size
    """
    def __init__(self, size):
        """
        Initializes the Square instance with a size.

        Args:
            size (int): The size of the square.

        Attributes:
            __size (int): Private attribute storing the size of the square.
        """
        self.__size = size

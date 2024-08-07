#!/usr/bin/python3
"""
Module - Square
"""


class Square:
    """
    Defines a square with a private instance attribute size and size
    validation.
    """
    def __init__(self, size=0):
        """
        Initializes the Square instance with a size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Attributes:
            __size (int): Private attribute storing size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

#!/usr/bin/python3
"""
Module - Square
"""


class Square:
    """
    Defines a square with a private instance attribute size, size validation,
    area calculation, getter and setter for size.
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
            __size (int): Private attribute storing the size of the square.
        """
        self.size = size  # Calls the setter method for validation

    @property
    def size(self):
        """
        Getter method to retrieve the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

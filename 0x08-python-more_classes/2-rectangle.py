#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """class: Rectangle this is an empty class
    """

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """method: set_width getterfor the private instance attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate perimeter of Rectangle object.
        """
        if self.__height == 0 or self.width == 0:
            return 0
        return (self.__height + self.width) * 2

#!/usr/bin/python3
"""
a class BaseGeometry (based on 5-base_geometry.py).
"""

class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

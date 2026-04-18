# 
# File: ball.py
# Author: Gunjan Rajak
# Student Id: a3183498
# Description: Ball class
# This is my own work as defined by the College's
# Academic Integrity Policy
#  

from shape3D import Shape3D
from math import pi

class Ball(Shape3D):
    """Inherits from Shape3D class. Uses a single side length to set all width, depth and height."""
    def __init__(self, width):
        super().__init__(width, width, width)
        self.radius = width / 2

    @property
    def radius(self):
        return self.__radius 
    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    def volume(self):
        return 4 * pi * self.radius * self.radius * self.radius / 3
    
    def area(self):
        return 4 * pi * self.radius * self.radius
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
    """Inherits from Shape3D class. Uses a single side length to set all width, depth and height. Returns area and volume of ball."""
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
    
    # Commented out __str__ because implemented __str__ methods to abstract base classes for polymorphism
    # def __str__(self):
    #     return f"Ball {self.width} X {self.width} X {self.width}\nArea: {self.area()}\nVolume: {self.volume()}"
    
# test code
if __name__ == "__main__":
    shapes = [
        Ball(4),
        Ball(5),
        Ball(3)
    ]
    for shape in shapes:
        print(shape)
        pass
    pass
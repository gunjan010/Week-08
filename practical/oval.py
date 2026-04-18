# 
# File: oval.py
# Author: Gunjan Rajak
# Student Id: a3183498
# Description: Oval class
# This is my own work as defined by the College's
# Academic Integrity Policy
#  

from shape2D import Shape2D
from math import pi

class Oval(Shape2D):
    '''Inherits from Shape2D. Calling an instance of this class return the area of the oval. '''
    def area(self):
        return pi * self.width_radius * self.height_radius

    def __str__(self):
        return f"Oval {self.width} X {self.height}\nArea: {self.area()}"

    # getter properties
    @property
    def width_radius(self) -> float:
        return self.width / 2
    @property
    def height_radius(self) -> float:
        return self.height / 2
    
# test code 
if __name__ == "__main__":
    shapes = [
        Oval(3, 4),
        Oval(2, 5),
        Oval(4, 6)
    ]
    for shape in shapes:
        print(shape)
        pass
    pass
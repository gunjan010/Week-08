# 
# File: polymorphism.py
# Author: Gunjan Rajak
# Student Id: a3183498
# Description: test all classes and polymorphism
# This is my own work as defined by the College's
# Academic Integrity Policy
#  

from square import Square, Rectangle
from circle import Circle, Oval
from cube import Cube, Box
from ball import Ball

if __name__ == "__main__":
    shapes_2d = [
        Rectangle(3, 4),
        Square(3),
        Circle(4),
        Oval(2, 4)
    ]
    shapes_3d = [
        Cube(5),
        Box(3, 4, 2),
        Ball(4),
        Cube(3),
        Ball(2),
        Box(2, 5, 4)
    ]

    shapes = shapes_2d + shapes_3d
    for shape in shapes:
        print(shape)
        pass

    pass
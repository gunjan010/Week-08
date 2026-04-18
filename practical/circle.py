# 
# File: circle.py
# Author: Gunjan Rajak
# Student Id: a3183498
# Description: Circle class
# This is my own work as defined by the College's
# Academic Integrity Policy
#  

from oval import Oval

class Circle(Oval):
    """Inherits from Oval class. Uses a single side as radius to set both width and height attributes."""
    def __init__(self, height):
        super().__init__(height, height)
        self.height = height

    # Commented out __str__ because implemented __str__ methods to abstract base classes for polymorphism
    # def __str__(self):
    #     return f"Circle {self.height} X {self.height}\nArea: {self.area()}"
    
# test code 
if __name__ == "__main__":
    shapes = [
        Circle(3),
        Oval(3, 2),
        Oval(2, 4),
        Circle(4)
    ]
    for shape in shapes:
        print(shape)
        pass
    pass
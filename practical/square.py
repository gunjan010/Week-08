# 
# File: square.py
# Author: Gunjan Rajak
# Student Id: a3183498
# Description: Square class
# This is my own work as defined by the College's
# Academic Integrity Policy
#  

from rectangle import Rectangle

class Square(Rectangle):
    """Inherits from Rectangle class. Uses a single side length to set both width and height."""
    def __init__(self, height):
        super().__init__(height, height)
        self.height = height

    def __str__(self):
        return f"Square {self.height} X {self.height}\nArea: {self.area()}"

# test code
if __name__ == "__main__":
    shapes = [
        Square(4),
        Rectangle(2, 3),
        Rectangle(6, 3),
        Square(5)
    ]
    for shape in shapes:
        print(shape)
        pass
    pass

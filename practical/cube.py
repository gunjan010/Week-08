# 
# File: cube.py
# Author: Gunjan Rajak
# Student Id: a3183498
# Description: Cube class
# This is my own work as defined by the College's
# Academic Integrity Policy
#  

from box import Box

class Cube(Box):
    """Inherits from Box class. Uses a single side length to set all width, depth and height."""
    def __init__(self, height):
        super().__init__(height, height, height)
        self.height = height

    def __str__(self):
        return f"Cube {self.height} X {self.height} X {self.height}\nArea: {self.area()}\nVolume: {self.volume()}"

# test code
if __name__ == "__main__":
    shapes = [
        Cube(4),
        Box(2, 3, 4),
        Box(2, 5, 3),
        Cube(5)
    ]
    for shape in shapes:
        print(shape)
        pass
    pass
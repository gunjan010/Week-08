# 
# File: box.py
# Author: Gunjan Rajak
# Student Id: a3183498
# Description: Box class
# This is my own work as defined by the College's
# Academic Integrity Policy
#  

from shape3D import Shape3D

class Box(Shape3D):
    '''Inherits from Shape3D. Calculates both area and volume of box'''
    def area(self):
        area_1 = self.width * self.height
        area_2 = self.width * self.depth
        area_3 = self.depth * self.height
        half_surface_area = area_1 + area_2 + area_3
        return 2 * half_surface_area
        
    def volume(self):
        return self.width * self.height * self.depth

    # Commented out __str__ because implemented __str__ methods to abstract base classes for polymorphism
    # def __str__(self):
    #     return f"Box {self.width} X {self.height} X {self.depth}\nArea: {self.area()}\nVolume: {self.volume()}"

# test code
if __name__ == "__main__":
    shapes = [
        Box(3, 4, 2),
        Box(4, 2, 5)
    ]
    for shape in shapes:
        print(shape)
        pass
    pass
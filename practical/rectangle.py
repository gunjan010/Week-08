# 
# File: rectangle.py
# Author: Gunjan Rajak
# Student Id: a3183498
# Description: Rectangle class
# This is my own work as defined by the College's
# Academic Integrity Policy
#  

from shape2D import Shape2D

class Rectangle(Shape2D):
    '''returns the area of rectangle by making use of abstract method(area) from Shape2D class'''
    def area(self) -> float: 
        return self.width * self.height
    
    # Commented out __str__ because implemented __str__ methods to abstract base classes for polymorphism
    # def __str__(self):
    #     return f"Rectangle {self.width} X {self.height}\nArea: {self.area()}"

# test code
if __name__ == "__main__":
    shapes = [
        Rectangle(3, 4),
        Rectangle(5, 6),
        Rectangle(2, 3)
    ]
    for shape in shapes:
        print(shape)
        pass
    pass
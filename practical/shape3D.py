# 
# File: shape3D.py
# Author: Gunjan Rajak
# Student Id: a3183498
# Description: Shape3D class
# This is my own work as defined by the College's
# Academic Integrity Policy
#  

from shape2D import Shape2D, ABC, abstractmethod

class Shape3D(Shape2D, ABC):
    '''Abstract base class for all 3D shapes. 
        Inherits from Shape2D and introduces depth as an additional dimension/attribute'''
    def __init__(self, width, height, depth):
        super().__init__(width, height)
        self.depth = depth

    @abstractmethod
    def volume(self) -> float:
        raise NotImplementedError()

    # getter
    @property
    def depth(self):
        return self.__depth
    # setter
    @depth.setter
    def depth(self, depth):
        self.__depth = depth

    # Overwriting the __str__ method
    def __str__(self) -> str:
        return "\n".join([
            " ".join([
                self.__class__.__name__,
                " x ".join([
                    str(self.width),
                    str(self.height),
                    str(self.depth)
                ])
            ]),
            " ".join([
                "Area:",
                str(self.area())
            ]),
            " ".join([
                "Volume:",
                str(self.volume())
            ])
        ])
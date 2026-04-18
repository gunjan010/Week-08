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
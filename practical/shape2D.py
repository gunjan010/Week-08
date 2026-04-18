from abc import ABC, abstractmethod

class Shape2D(ABC):
    '''abstract class with width, height and abstract area method'''
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @abstractmethod
    def area(self) -> float:
        raise NotImplementedError

    # getters
    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height
    
    # setters
    @width.setter
    def width(self, width):
        self.__width = width
    @height.setter
    def height(self, height):
        self.__height = height
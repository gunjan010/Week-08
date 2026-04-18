from abc import ABC, abstractmethod

class Shape2D(ABC):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @abstractmethod
    def area(self) -> float:
        pass

    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height
    
    @width.setter
    def width(self, width):
        return width
    @height.setter
    def height(self, height):
        return self.__height
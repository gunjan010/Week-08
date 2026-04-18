from shape2D import Shape2D

class rectangle(Shape2D):
    '''returns the area of rectangle by making use of abstract method(area) from Shape2D class'''
    def area(self):
        return self.width * self.height

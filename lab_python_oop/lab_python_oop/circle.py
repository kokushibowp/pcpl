from .geometric_shape import GeometricShape
from .shape_color import ShapeColor
import math

class Circle(GeometricShape):
    
    __name = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = ShapeColor()
        self.color = color 

    def area(self):
        return math.pi*(self.radius)*(self.radius)
    
    def get_name(self):
        return self.__name
    
    def get_color(self):
        if(self.color == ShapeColor.RED):
            return "красный"
        elif(self.color == ShapeColor.GREEN):
            return "зеленый"
        elif(self.color == ShapeColor.BLUE):
            return "синий"
    
    def __repr__(self):
        return "Площадь круга: {} Цвет круга: {}".format(self.area(), self.get_color())
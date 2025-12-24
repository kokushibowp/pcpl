from .geometric_shape import GeometricShape
from .shape_color import ShapeColor

class Rectangle(GeometricShape):

    __name = "Прямоугольник"

    def __init__(self, x, y, color):
        self.x =  x
        self.y = y
        self.color = ShapeColor()
        self.color = color

    def area(self):
        return self.x*self.y
    
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
        return "Площадь прямоугольника: {} Цвет прямоугольника: {}".format(self.area(), self.get_color())
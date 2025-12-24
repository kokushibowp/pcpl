from .rectangle import Rectangle
from .shape_color import ShapeColor

class Square(Rectangle):

    __name = "Квадрат"

    def __init__(self, x, color):
        self.x = x
        self.color = ShapeColor()
        self.color = color

    def area(self):
        return self.x*self.x
    
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
        return "Площадь квадрата: {} Цвет квадрата: {}".format(self.area(), self.get_color())
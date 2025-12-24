class ShapeColor:
    RED = 1
    GREEN = 2
    BLUE = 3

    def __init__(self):
        self._color = None

    def getColor(self):
        return self._color
    
    def setColor(self, value):
        self._color = value

    def delColor(self):
        del self._color

    color = property(getColor, setColor, delColor)
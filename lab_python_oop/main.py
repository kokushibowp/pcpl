import lab_python_oop as lpo
import requests

def main():
    circle = lpo.Circle(1, 2)
    rectangle = lpo.Rectangle(1, 1, 3)
    square = lpo.Square(1, 1)
    print(circle)
    print(rectangle)
    print(square)


if(__name__ == "__main__"):
    main()
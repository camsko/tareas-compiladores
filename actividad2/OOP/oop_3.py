# Clase con constructor y parámetros

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

rec = Rectangle(10, 20)

print(f'Rectangle: ({rec.width}, {rec.height})')


# Clase con métodos básicos (Sin estado)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def dimension(self):
        return 2

rec = Rectangle(10, 20)

print(f'Rectangle: ({rec.width}, {rec.height}) with dimension {rec.dimension()}')
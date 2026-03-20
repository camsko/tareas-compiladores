# Herencia con super

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
    
    def area(self):
        return self.width * self.height
    
    def identity(self):
        return f'Square of side length {self.width} and area {self.area()}'

sq = Square(5)

print(sq.identity())



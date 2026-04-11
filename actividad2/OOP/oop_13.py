# Clase con métodos dunder de operaciones matemáticas

def get_number_value(num: Number | int | float):
    if isinstance(num, Number):
        return num.value
    return num

class Number:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other: Number | int | float):
        return Number(self.value + get_number_value(other))
    
    def __sub__(self, other: Number | int | float):
        return Number(self.value - get_number_value(other))
    
    def __mul__(self, other: Number | int | float):
        return Number(self.value * get_number_value(other))
    
    def __truediv__(self, other: Number | int | float):
        return Number(self.value / get_number_value(other))
    
    def __pow__(self, other: Number | int | float):
        return Number(self.value ** get_number_value(other))
    
    def __repr__(self):
        return f'Class Number with value {self.value}'

a = Number(5)
b = Number(12)

print(a + b)
print(a + 3)
print(a - b)
print(a - 3)
print(a * b)
print(a * 3)
print(a / b)
print(a / 3)
print(a ** b)
print(a ** 3)
# Clase con métodos dunder de operaciones matemáticas in-place

def get_number_value(num: Number | int | float):
    if isinstance(num, Number):
        return num.value
    return num

class Number:
    def __init__(self, value):
        self.value = value
    
    def __iadd__(self, other: Number | int | float):
        self.value += get_number_value(other)
        return self
    
    def __isub__(self, other: Number | int | float):
        self.value -= get_number_value(other)
        return self
    
    def __imul__(self, other: Number | int | float):
        self.value *= get_number_value(other)
        return self
    
    def __itruediv__(self, other: Number | int | float):
        self.value /= get_number_value(other)
        return self
    
    def __ipow__(self, other: Number | int | float):
        self.value **= get_number_value(other)
        return self
    
    def __repr__(self):
        return f'Class Number with value {self.value}'

a = Number(5)
b = Number(12)

print(a)
a += b
print(a)
a -= b
print(a)
a *= b
print(a)
a /= b
print(a)
a **= b
print(a)

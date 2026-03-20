# Clase con métodos dunder de condicionales

def get_number_value(num: Number | int | float):
    if isinstance(num, Number):
        return num.value
    return num

class Number:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other: Number | int | float):
        return self.value == get_number_value(other)
    
    def __ne__(self, other: Number | int | float):
        return self.value != get_number_value(other)
    
    def __lt__(self, other: Number | int | float):
        return self.value < get_number_value(other)
    
    def __gt__(self, other: Number | int | float):
        return self.value > get_number_value(other)
    
    def __le__(self, other: Number | int | float):
        return self.value <= get_number_value(other)
    
    def __ge__(self, other: Number | int | float):
        return self.value >= get_number_value(other)

a = Number(5)
b = Number(5)

print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
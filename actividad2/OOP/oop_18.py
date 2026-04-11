# Clase con método dunder __repr__

class Number:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f'{self.value}'
    
a = Number(5)

print(a)
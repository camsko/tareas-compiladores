# Clase con método dunder __str__

class Number:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f'{self.value}'
    
a = Number(5)

print(str(a))
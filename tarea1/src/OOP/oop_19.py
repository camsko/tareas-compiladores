# Clase con método dunder __call__

class LinearFunction:
    def __init__(self, m = 1, b = 0):
        self.m = m
        self.b = b
    
    def __call__(self, x):
        return self.m * x + self.b
    
f = LinearFunction(3, 2)

print(f(5))
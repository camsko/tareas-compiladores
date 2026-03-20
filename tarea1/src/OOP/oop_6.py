# Clase con métodos que llaman a otros métodos

class Functions:
    def f(self, x):
        return 10 * x
    
    def g(self, x):
        return self.f(x + 5)
    
funcs = Functions()

print(funcs.g(3))



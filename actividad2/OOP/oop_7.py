# Herencia básica

class A:
    a = 10

class B(A):
    b = 11
    def f(self):
        return f"{self.a}, {self.b}"
    
print(B().f())
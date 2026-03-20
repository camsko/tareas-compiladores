# Herencia múltiple

class A:
    a = 10

class B(A):
    b = 11

class C(A):
    c = 12

class D(B, C):
    def f(self):
        return f"{self.a}, {self.b}, {self.c}"
    

print(D().f())
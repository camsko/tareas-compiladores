# MRO con herencia múltiple (Invertido)

class A:
    def test(self):
        return 'Clase A'
    
class B(A):
    def test(self):
        return 'Clase B'

class C(A):
    def test(self):
        return 'Clase C'

class D(C, B):
    pass
    
obj = D()

print(obj.test())
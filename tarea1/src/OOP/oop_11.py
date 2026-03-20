# MRO con múltiple herencia

class A:
    def test(self):
        return 'Clase A'
    
class B(A):
    def test(self):
        return 'Clase B'

class C(A):
    def test(self):
        return 'Clase C'

class D(B, C):
    pass
    
obj = D()

print(obj.test())
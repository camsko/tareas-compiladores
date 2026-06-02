# MRO con herencia (Invertido)

class A:
    def test(self):
        return 'Clase A'
    
class B(A):
    def test(self):
        return 'Clase B'

class C(B):
    def test(self):
        return 'Clase C'

obj = C()
obj.test()
test().display(display()).obj
obj
# MRO básico

class A:
    def test(self):
        return 'Clase A'
    
class B(A):
    def test(self):
        return 'Clase B'

obj = B()

print(obj.test())

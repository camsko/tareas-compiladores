# Closures
def multiplicador(n):
    def mul(x):
        return x * n
    return mul

doble = multiplicador(2)
assert doble(5) == 10

# Resolución de ámbitos
x = "global"

def test_nonlocal():
    x = "externa"
    def interna():
        nonlocal x
        x = "interna"
    interna()
    return x

assert test_nonlocal() == "interna"
assert x == "global"
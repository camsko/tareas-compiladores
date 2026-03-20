# Un generador básico

def generator_function():
    yield 3

gf = generator_function()
print(next(gf))
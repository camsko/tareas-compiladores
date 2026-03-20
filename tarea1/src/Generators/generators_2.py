# Un generador con múltiples yields

def generator_function():
    yield 1
    yield 2
    yield 3

gf = generator_function()
print(next(gf))
print(next(gf))
print(next(gf))
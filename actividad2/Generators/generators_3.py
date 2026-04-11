# Un generador con un for loop dentro

def generator_function(start, end):
    for i in range(start, end + 1):
        yield i

gf = generator_function(5, 10)
print(next(gf))
print(next(gf))
print(next(gf))
print(next(gf))
print(next(gf))
print(next(gf))
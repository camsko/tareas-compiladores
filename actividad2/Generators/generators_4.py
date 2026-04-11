# Un generador con un for loop dentro y afuera

def generator_function(start, end):
    for i in range(start, end + 1):
        yield i

gf = generator_function(5, 10)

for i in gf:
    print(i)
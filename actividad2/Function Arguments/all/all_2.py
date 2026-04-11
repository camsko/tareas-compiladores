def funcion(a, b=10, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

funcion(1)
print("_____________________________")
funcion(1, 2, 3, 4, x=5, y=6)
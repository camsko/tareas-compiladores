#adaptado de https://www.geeksforgeeks.org/python/scope-resolution-in-python-legb-rule/

var = "global value"

def outer():
    var = "outer value"
    def inner():
        var = "inner value"

        print("Inner:", var)
    inner()
    print("Outer:", var)


outer()
print("Global:", var)
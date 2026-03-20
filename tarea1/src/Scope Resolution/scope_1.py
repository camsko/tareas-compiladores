var = "global value"

def func():
    var = "local value"
    print(var)

func()
print(var)
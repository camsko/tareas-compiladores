var = 5.
text = "Hola Mundo"
var2 = 0
var2 += var 
var //= 5 
var **= 5
var += 5 
var -= 5 
var *= 5 
var /= 5 
var %= 5 

class MyClass:
    def __init__(self, x):
        self.x = x

class ChildClass(MyClass):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

def ejemplo(x, y=5, z=5.5):
    var = x

if (var == 0) and (var2 == 0 or var == var2):
    var = 4
    if var == 0:
        var = 1
elif var == 0:
    var = 0
else:
    var = 0

while (var >= 0) and (var2 == 0 or var <= var2): 
    var = 0
    var = 1
    var = 2

for i in range(10):
    var = i
    
for i in range(0, var):
    var = i
    
for i in [1, 2, 3]:
    var = i
    
for i in (10, 20, 30):
    var = i

for i in {"a": 1, "b": 2}:
    var = i
    
for i in var:
    var = i

var = [1, 2, 3]

var = (10, 20, 30)

var = {"a": 1, "b": 2}

5 = 5
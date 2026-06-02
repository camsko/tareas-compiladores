a = 2 ** 3 + 10 * 5 - 4 // 2 % 3
b = (a + 2) * (a - 1) / (a % 3 + 1)
c = ((2 + 3) * (4 - 1)) ** 2 // (7 % 3 + 1)

a = 3

"hello" + 4 + "world"
for i in range(10):
    if i % 2 == 0 and i > 5:
        print(i)
    elif i % 3 == 0 or i < 3:
        print(i * 2)
        break
        continue
        pass
    else:
        print(i ** 2)
function.myarg(arg1, arg2)
def function(arg1, arg2):
    return arg1 + arg2
class MyClass:
    def __init__(self, x: int| str):
        self.x = x

    def method1(self, y):
        return self.x + y

    def method2(self, z):
        return self.x * z

function.method(arg1, arg2, arg1 + arg2, not arg1 and arg2)


check1 = x + 5 > y - 3 > 4 and z * 2 <= 100 or not x == y
check2 = (x ** 2 + y ** 2 >= z ** 2) and not (x * y == z * 2)
check3 = not (x + y > z and y - x < z) or (z % x == 0 and z // y != 1)

deep1 = ((x + (y * (z - 2))) ** 2) // ((z % (x + 1)) + 1)
deep2 = (((x + y) * z) - ((x - y) * z)) / ((x * y) - (y * z) + 1)
deep3 = not ((x + y >= z or x * y <= z ** 2) and (z // x != y % x or x == y - 10))
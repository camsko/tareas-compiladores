n = 10

if n <= 0:
    print("Invalid input")
elif n == 1:
    print(0)
else:
    a = 0
    b = 1

    print(a)
    print(b)

    for i in range(2, n):
        c = a + b
        print(c)
        a = b
        b = c
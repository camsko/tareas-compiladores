x = 4
y = 3
z = 2
a = x + 1
b = a - 2
c = b / 1
d = c * 3
e = True

if (x == 4 and (z <= 3 or y <= 5)):
    print(False)
elif(x == 5):
    print(False)
else:
    print(True)
    
while (x > 4):
    print(True)
    
for i in z:
    print(i)
    
for i in range(2,10):
    print(i)

if (((a >= d) or b <= 2) and ((c != b) or (d < 10))):
    print(True)
    
elif (not e):
    print(False)

else:
    print(True)
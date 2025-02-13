import math
x1, y1 = 0,2
x2, y2 = 0,3
x3, y3 = 0,1
x4, y4 = 0,4

a = ((x2-x1)**2 + (y2-y1)**2)**0.5
b = ((x3-x2)**2 + (y3-y2)**2)**0.5
c = ((x4-x3)**2 + (y4-y3)**2)**0.5
d = ((x1-x4)**2 + (y1-y4)**2)**0.5

diag = ((x3-x1)**2+(y3-y1)**2)**0.5
diag2 = ((x4-x2)**2+(4-y2)**2)**0.5

if a == b == c == d:
    if diag == diag2:
        print("квадрат")
    else:
        print("ромб")
elif a==c and b==d :
    if diag == diag :
        print('прямоуголник')
    else:
        print("параллелограм")
else:
    print('хз что это')
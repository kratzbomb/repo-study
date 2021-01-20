a = float(input())
b = float(input())
c = float(input())
from math import *
d = b ** 2 - 4 * a * c
if a != 0:
    if d > 0:
        x1 = ((- b) + sqrt(d)) / (2 * a)
        x2 = ((- b) - sqrt(d)) / (2 * a)
        print(min(x1, x2))
        print(max(x1, x2))
    elif d == 0:
        x1 = -(b / (2 * a))
        print(x1)
    elif d < 0:
        print("Нет корней")
else:
    print("ошибка")
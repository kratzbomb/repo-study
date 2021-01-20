p1 = 1
p2 = 1
n = int(input())
if n == 1:
    print(p1)
elif n == 2:
    print(p1, p2)
elif n > 2:
    a = p1
    b = p2
    print(a, b, end =" ")
    for i in range(2, n):
        p1, p2 = p2, p1 + p2
        print(p2, end = ' ')


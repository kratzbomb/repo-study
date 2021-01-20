a = int(input())
b = int(input())
c = int(input())
d = int(input())
if abs(a - c) == abs(b - d):
    print("YES")
elif a == c and b != d or b == d and a != c:
    print("YES")
else:
    print("NO")

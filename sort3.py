a, b, c, = int(input()), int(input()), int(input())
n = min(a, b, c)
m = max(a, b, c)
if n == a:
    if m == b:
        print(b, c, a, sep='\n')
    else:
        print(c, b, a, sep='\n')
elif n == b:
    if m == a:
        print(a, c, b, sep='\n')
    else:
        print(c, a, b, sep='\n')
elif n == c:
    if m == a:
        print(a, b, c, sep='\n')
    else:
        print(b, a, c, sep='\n')
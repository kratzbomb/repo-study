a = int(input())
if a < 0 or a > 36:
    print('ошибка ввода')
elif a == 0:
    print("зеленый")
else:
    if 1 <= a <= 10 and a % 2 == 0:
        print('черный')
    elif 1 <= a <= 10 and a % 2 != 0:
        print('красный')
if 11 <= a <= 18 and a % 2 == 0:
        print('красный')
elif 11 <= a <= 18 and a % 2 != 0:
        print('черный')
if 19 <= a <= 28 and a % 2 == 0:
        print('черный')
elif 19 <= a <= 28 and a % 2 != 0:
        print('красный')
if 29 <= a <= 36 and a % 2 == 0:
        print('красный')
elif 29 <= a <= 36 and a % 2 != 0:
        print('черный')
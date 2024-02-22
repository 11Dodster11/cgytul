a = int(input("Введите 1-ое число: "))
b = int(input("Введите 2-ое число: "))
c = int(input("Введите 3-е число: "))

if a == b or a == c or b == c:
    print("Ошибка")
else:
    if (a < b and b < c) or (c < b and b < a):
        print(f"Число {b} стоит между числами {a} и {c}")
    elif (b < a and a < c) or (c < a and a < b):
        print(f"Число {a} стоит между числами {b} и {c}")
    elif (a < c and c < b) or (b < c and c < a):
        print(f"Число {c} стоит между числами {a} и {b}")
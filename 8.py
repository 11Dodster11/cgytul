year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "високосный год")
    days = 366
else:
    print(year, "не високосный год")
    days = 365

print("Количество дней в году:", days)
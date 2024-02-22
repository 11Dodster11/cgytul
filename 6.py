x = float(input("Введите координату x точки: "))
y = float(input("Введите координату y точки: "))
radius = float(input("Введите радиус круга: "))

distance = (x ** 2 + y ** 2) ** 0.5

if distance <= radius:
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")
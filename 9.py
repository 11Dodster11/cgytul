d = int(input("Введите дальность выстрела "))
if d > 28 and d < 30:
	print("Попал")
if d >= 30:
	print("Перелёт")
if d > 0 and d <= 28:
	print("Недолёт")
if d <= 0:
	print("Не бей по своим")
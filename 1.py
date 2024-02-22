a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
	print("Максимальное число: ",a)
if b > c and b > a:
	print("Максимальное число: ",b)
if c > b and c > a:
	print("Максимальное число: ",c)
#1


numbers = [1, 2, 3, 4, 5, 2, 3, 4, 6, 7, 7, 8, 9, 10]

unique_numbers = set(numbers)
count = len(unique_numbers)

print("Ежже разных чисел:", count)

#2

n = [1, 2, 3, 4, 5, 2, 3, 4, 6, 7, 7, 8, 9, 10]
s = [1, 2, 2, 3, 9, 11, 4, 5, 6, 7, 8, 11, 9, 100]

u_n = set(n)
c = len(u_n)

u_s = set(s)
a = len(u_s)

print("Ежже разных чисел списке:", c+a)

#3

l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

a1 = set(l1)
a2 = set(l2)

n = sorted(list(a1 & a2))

print("Схожие числа в 2ух списках:", n)

#4

s = input("Введите последовательность чисел через пробел: ")
ns = s.split()

s_n = set()

for n in ns:
    if n in s_n:
        print("YES")
    else:
        print("NO")
        s_n.add(n)
        
        
#5

f = open("input.txt", "r")
t = f.read()
w = t.replace("\n", " ").split()
wo = set(w)
c = len(wo)
print("Количество различных слов:", c)

from random import randint
list1 = []
n = int(input('Введите количество (n): '))
for i in range(0, n):
    list1.append(randint(-100, 100))
print(list1)

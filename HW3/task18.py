# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# n = 5
# 1 2 3 4 5
# x = 6
# -> 5
import random
n = int(input('Введите количество элементов в массиве '))
list = []
for i in range(n):
    list.append(random.randint(0, 10))
print(list)
x = int(input('Искомое число '))
dif, closest = abs(list[0]-x), list[0]
for i in range(len(list)):
    if abs(list[i]-x) < dif:
        dif, closest = abs(list[i]-x), list[i]
print(closest, "- Cамый близкий по величине элемент к заданному числу -", x)

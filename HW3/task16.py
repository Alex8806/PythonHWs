# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 3

# -> 1
import random
n = int(input('Введите количество элементов в массиве '))
list = []
for i in range(n):
    list.append(random.randint(-10, 10))
print(list)
x = int(input('Искомое число '))
count = 0
for i in range(len(list)):
    if x == list[i]:
        count += 1
print('Чило', x, "Встречается", count, "раз")
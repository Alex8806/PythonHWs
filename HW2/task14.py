# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input('Введите число '))
if n<1:
    print("Таких чисел нет")
else:
    x, i = 1 , 0
    while x < n:
         print(x)
         i+=1
         x = 2**i 
# Петя успевает по математике лучше всех в классе, поэтому учитель задал ему сложное домашнее задание,
# в котором нужно в заданном наборе целых чисел найти сумму всех положительных элементов,
# затем найти где в заданной последовательности находятся максимальный и минимальный элемент
# и вычислить произведение чисел, расположенных в этой последовательности между ними.
# Так же известно, что минимальный и максимальный элемент встречаются
# в заданном множестве чисел только один раз и не являются соседними.
# Поскольку задач такого рода учитель дал Пете около ста,
# то Петя как сильный программист смог написать программу,
# которая по заданному набору чисел самостоятельно находит решение. А Вам слабо?

# Входные данные
# В первой строке входного файла INPUT.TXT записано единственное число N – количество элементов массива.
# Вторая строка содержит N целых чисел, представляющих заданный массив.
# Все элементы массива разделены пробелом. Каждое из чисел во входном файле, в том числе и N,
# не превышает 102 по абсолютной величине.

# Выходные данные
# В единственную строку выходного файла OUTPUT.TXT нужно вывести два числа,
# разделенных пробелом: сумму положительных элементов и произведение чисел,
# расположенных между минимальным и максимальным элементами.
# Значения суммы и произведения не превышают по модулю 3*104.
if (input("Хотите перезаписать input.txt (YES/NO) - ").upper() == "YES"):
    data = open('HW5/input.txt', 'w')
    n = input(" N – количество элементов массива - ")
    data.writelines(f'{n}\n')
    list = [input(f'Вваедите {i+1} элемент - ') for i in range(int(n))]
    data.writelines(' '.join(list))
    data.close()

with open('HW5/input.txt', 'r') as data:
    n = int(data.readline())
    list = [int(i)for i in data.readline().split()]
    print(n, list)
    data.close()

maxindex, minindex, max, min = 0, 0, list[0], list[0]
for i in range(len(list)):
    if list[i] > max:
        maxindex, max = i, list[i]
    if list[i] < min:
        minindex, min = i, list[i]

sum, multip = 0, 1
if minindex > maxindex:
    maxindex, minindex = minindex, maxindex
for i in range(minindex+1,maxindex):
    sum+=list[i]
    multip*=list[i]
print(sum , multip)

data = open('HW5/output.txt', 'w')
data.writelines(f'{sum} {multip}')
data.close()

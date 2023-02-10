# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
import random
m = 0
while m < 3:
    m = int(input('Кол-во кустов '))
    if m < 3:
        print("Ведите больше двух кустов")


def filling(p):
    list = []
    for i in range(p):
        list.append(random.randint(0, 15))
    return list


bushes = filling(m)
print(f'Количество ягод на кустах {bushes}')
maxsumm, index, temp = 0, {}, 0
for i in range(-1, len(bushes)-1):
    temp = bushes[i-1]+bushes[i]+bushes[i+1]
    if i == -1:
        i = len(bushes)-1
    if temp == maxsumm:
        index.add(i+1)
    if temp > maxsumm:
        maxsumm, index = temp, {i+1}

x = ' или '.join(map(str, index))
print(f'Максимум ягод {maxsumm} на кусте {x}')

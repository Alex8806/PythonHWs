# Задача №1461. Шарики
# В одной компьютерной игре игрок выставляет в линию шарики разных цветов.
# Когда образуется непрерывная цепочка из трех и более шариков одного цвета, она удаляется из линии.
#  Все шарики при этом сдвигаются друг к другу, и ситуация может повториться.
# Напишите программу, которая по данной ситуации определяет, сколько шариков будет "уничтожено".
# Естественно, непрерывных цепочек из трех и более одноцветных шаров в начальный момент
# может быть не более одной.
# Входные данные
# A
# Сначала вводится количество шариков в цепочке (не более 1000) и цвета шариков (от 0 до 9, каждому цвету соответствует свое целое число).
# о
# Ө
# Выходные данные
# Требуется вывести количество шариков, которое будет "уничтожено".
# Примеры
# входные данные
# 5 1 3 3 3 2
# выходные данные
import random
m = int(input('Кол-во шариков '))


def filling(p):
    list = []
    for i in range(p):
        list.append(random.randint(0, 1))
    return list


def matching(list):
    count, flag, temp = 0, False, -1
    for i in range(1, len(list)-1):
        if list[i-1] == list[i] == list[i+1]:
            count += 1
            flag  = True
            temp = i
        elif flag == True:
            break
    if count > 0:
        del list[(temp-count):(temp+2)]
        print(f"Уничтожено {count+2} шарикa")
    else:
        print("Совпадений нет")
    return list


list = filling(m)
print("Выпали шарики", list)
while (name := input("Для проверки напишите  'check' ") == 'check'):
    list = matching(list)
    print("Остались шарики ", list)

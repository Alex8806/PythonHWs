# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
n = int(input('Введите число монеток - '))
count0, count1 = 0 , 0
for i in range(n):
    storona = 2
    while storona != 1 and storona != 0 :
        storona = int(input("Как повернута монетка 0-решка, 1-орел? " ))
        if storona != 1 and storona != 0:
            print("Ошибка. Попробуй еще раз!")
    if storona == 1: count1 += 1
    elif storona == 0: count0 += 1
if count1 != count0:
    if count1<count0:
        side = 'орел'
    else:
        side = 'решка'
    print(f'минимальное количество монет, которые нужно перевернуть - {min(count1, count0) } повернутыне сотороной {side}')
else:
    print(f'Переворачивайте что хотите. Количество монет, которые нужно перевернуть {count0}')
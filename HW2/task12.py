# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3
s , p = int(input("Cумма  чисел ")) , int(input("Произведение  чисел "))


d = s**2 - 4 * p
if d >= 0:
    x = (s+d**0.5)/2 
    print(f'числа { x } и { s - x } ')
elif d<0:
    print('Петя обманщик! Такого не может быть!')
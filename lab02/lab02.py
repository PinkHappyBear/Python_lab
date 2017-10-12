import math
from math import atan

dataa = input("Введите a:")
datab =input("Введите b:")
if dataa and datab:
    try:
        a = float(dataa)
        b = float(datab)
        print(a,b)
    except ValueError:
        print('Нужно было вводить число,но так как циклы мы ещё не проходили,break НЕ БУДЕТ,программа просто крашнется')
else:
    print('Введите число')

print(" 1 - Вычислить функцию G\n"
      " 2 - Вычислить функцию F\n"
      " 3 - Вычислить функцию Y\n"
      " Другое значение - Выход из программы")
num1 = float(input('Значение'))
if num1 == 1:
    G = (9 * (20 * (b ** 2) - 31 * a * b + 12 * (b ** 2))) / (10 * (a ** 2) - 17 * a * b + 6 * (b ** 2))
    print('A = {}.\nB = {}.\nРезультат: {}'.format(a,b,G))
elif num1 == 2:
    F = - atan (7 * (a ** 2) - 2 * a * b - 9 * (b ** 2))
    print('A = {}.\nB = {}.\nРезультат: {}'.format(a,b,F))
elif num1 == 3:
    Y = - atan (2 * (a ** 2) + (a * b) - 3 * (b ** 2))
    print('A = {}.\nB = {}.\nРезультат: {}'.format(a,b,Y))
else:
    print("Такого значения нет")
print("Нажмите любую клавишу для выхода из программы")
element = input("")
if element:
    try:
        element = float(element)
    except ValueError:
        print("Exit")
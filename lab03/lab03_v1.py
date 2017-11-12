from math import atan
from tkinter import *
num = 0
while num <= 3: # Объявляем цикл
    num = int(input("Введите 1 для рассчёта G\nВведите 2 для рассчёта F\nВведите 3 для рассчёта Y\nВведите любую другую цифру для выхода\n"))
    if num > 3 or num <= 0: # Если num не 1,2,3 - выход из цикла
        break
    a = float(input("Введите a:")) #Запрос входных значений
    print("Задайте границы изменения х:")
    min_x = float(input("От:"))
    max_x = float(input("До:"))
    while min_x >= max_x:
        max_x = float(input("Верхняя граница должна быть выше нижней\nДо:"))
    NumberOfSteps = int(input("Введите желаемое количество шагов:"))
    x = min_x
    if num == 1: # Если пользователь ввёл 1 - рассчитывает G
        print("Пожалуйста,подождите...")
        while x <= max_x:
            z = (10 * (x ** 2) - 17 * x * a + 6 * (a ** 2)) #Рассчёт знаменателя
            if z == 0:
                print("x = %.3f\tВходные значения не входят в область определения " % x)
                x += (max_x - min_x) / (NumberOfSteps - 1)
                continue
            G = (9 * (20 * (a ** 2) - 31 * x * a + 12 * (a ** 2))) / z
            print('x =%.3f\t\tG = %.3f'%(x,G))
            x += (max_x - min_x) / (NumberOfSteps - 1)
    elif num == 2:  # Если пользователь ввёл 2 - рассчитывает F
        print("Пожалуйста,подождите...")
        while x <= max_x:
            F = - atan (7 * (x ** 2) - 2 * x * a - 9 * (a ** 2))
            print('x = %.3f\tF = %.3f'% (x,F))
            x += (max_x - min_x) / (NumberOfSteps - 1)   
    elif num == 3: # Если пользователь ввёл 3 - рассчитывает Y
        print("Пожалуйста,подождите...")
        while x <= max_x:
            Y = - atan (2 * (x ** 2) + (x * a) - 3 * (a ** 2))
            print('x = %.3f\tY = %.3f' % (x, Y))
            x += (max_x - min_x) / (NumberOfSteps - 1)

from math import atan
from tkinter import *
num = 0
list =[] # Заранее создаём списки.Для удобства.
list_two = []
list_three =[]
while num <= 3: # Объявляем цикл
    num = int(input("Введите 1 для рассчёта G\nВведите 2 для рассчёта F\nВведите 3 для рассчёта Y\nВведите 4 для подсчёта целых чисел\nВведите любую другую цифру для выхода\n"))
    if num > 4 or num <= 0: # Если num не 1,2,3 - выход из цикла
        break
    
    if num == 4:
        number = input ("Введите число:")
        counter = 0
        if number.isdigit(): # Возвращает флаг,указывающий на то,содержит ли строка только цифры
            value = int(number)
            while value > 0:
                digit = value % 10 
                if digit % 2 == 0:
                    counter += 1
                value = int(value / 10 )
            print("Количество чётных цифр: %d" % counter)
            num = int(input("Введите 1 для рассчёта G\nВведите 2 для рассчёта F\nВведите 3 для рассчёта Y\nВведите 4 для подсчёта целых чисел\nВведите любую другую цифру для выхода\n"))
            continue
        
    a = float(input("Введите a:")) #Запрос входных значений
    print("Задайте границы изменения х:")
    min_x = float(input("От:"))
    max_x = float(input("До:"))
    while min_x >= max_x:
        max_x = float(input("Верхняя граница должна быть выше нижней\nДо:"))
    NumberOfSteps = int(input("Введите желаемое количество шагов:"))
    x = min_x
    result = ''
    if num == 1: # Если пользователь ввёл 1 - рассчитывает G
        print("Пожалуйста,подождите...")
        while x <= max_x:
            z = (10 * (x ** 2) - 17 * x * a + 6 * (a ** 2)) #Рассчёт знаменателя
            if z == 0:
                print("x = %.3f\tВходные значения не входят в область определения " % x)
                x += (max_x - min_x) / (NumberOfSteps - 1)
                continue
            G = (9 * (20 * (a ** 2) - 31 * x * a + 12 * (a ** 2))) / z
            list.append(G) # Добавляем элемент в список
            sys.stdout.write('G = %.3f '%(G))
            result += str(round(G, 3))
            x += (max_x - min_x) / (NumberOfSteps - 1)
        print('\nМинимальное значение G = %.3f' % min(list)) # Выводим минимальное и максимальное значение из списка
        print('Максимальное значение G = %.3f' % max(list))
    elif num == 2:  # Если пользователь ввёл 2 - рассчитывает F
        print("Пожалуйста,подождите...")
        while x <= max_x:
            F = - atan (7 * (x ** 2) - 2 * x * a - 9 * (a ** 2))
            list_two.append(F)
            sys.stdout.write('F = %.3f '%(F))
            result += str(round(F, 3))
            x += (max_x - min_x) / (NumberOfSteps - 1)
        print('Минимальное значение G = %.3f' % min(list_two))
        print('Максимальное значение G = %.3f' % max(list_two))    
    elif num == 3: # Если пользователь ввёл 3 - рассчитывает Y
        print("Пожалуйста,подождите...")
        while x <= max_x:
            Y = - atan (2 * (x ** 2) + (x * a) - 3 * (a ** 2))
            list_three.append(Y)
            sys.stdout.write('Y = %.3f '%(Y))
            result += str(round(Y, 3))
            x += (max_x - min_x) / (NumberOfSteps - 1)
        print('Минимальное значение G = %.3f' % min(list_three))
        print('Максимальное значение G = %.3f' % max(list_three))

    print('Строка: %s' % result)
    template = input("Задайте шаблон: ")
    counter = 0
    idx = result.find(template)  # Получаем индекс первого вхождения шаблона в строку
    while idx > -1:
        result = result[idx + 1:len(result) - 1]  # Обрезаем строку
        counter += 1  # Увеличиваем счетчик
        idx = result.find(template)  # Получаем новое вхождение
    print("Совпадений: %d." % counter)
    num = int(input("Введите 1 для рассчёта G\nВведите 2 для рассчёта F\nВведите 3 для рассчёта Y\nВведите 4 для подсчёта целых чисел\nВведите любую другую цифру для выхода\n"))

from math import atan
import sys
num = 0
result = ''
list =[] # Заранее создаём списки.Для удобства.
list_two = []
list_three =[]
#
while num == 0: # Объявляем цикл
    num = int(input("Введите 1 для рассчёта G\nВведите 2 для рассчёта F\nВведите 3 для рассчёта Y\nВведите любую другую цифру для выхода\n"))
    if num > 3 or num <= 0: # Если num не 1,2,3 - выход из цикла
        break       
    a = float(input("Введите a:")) #Запрос входных значений
    print("Задайте границы изменения х:")
    min_x = str(input("От:"))
    min_x = float(min_x)
    max_x = str(input("До:"))
    max_x = float(max_x)
    while min_x >= max_x:
        max_x = float(input("Верхняя граница должна быть выше нижней\nДо:"))
    NumberOfSteps = str(input("Введите желаемое количество шагов: "))
    NumberOfSteps = int(NumberOfSteps)
    x = min_x
#    
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
            print('G = %.3f '%(G)) # sys.stdout.write
            result += str(G)
            x += (max_x - min_x) / (NumberOfSteps - 1)
        print('\nМинимальное значение G = %.3f' % min(list)) # Выводим минимальное и максимальное значение из списка
        print('Максимальное значение G = %.3f' % max(list))
    elif num == 2:  # Если пользователь ввёл 2 - рассчитывает F
        print("Пожалуйста,подождите...")
        while x <= max_x:
            F = - atan (7 * (x ** 2) - 2 * x * a - 9 * (a ** 2))
            list_two.append(F)
            sys.stdout.write('F = %.3f '%(F))
            result += str(F)
            x += (max_x - min_x) / (NumberOfSteps - 1)
        print('Минимальное значение G = %.3f' % min(list_two))
        print('Максимальное значение G = %.3f' % max(list_two))    
    elif num == 3: # Если пользователь ввёл 3 - рассчитывает Y
        print("Пожалуйста,подождите...")
        while x <= max_x:
            Y = - atan (2 * (x ** 2) + (x * a) - 3 * (a ** 2))
            list_three.append(Y)
            sys.stdout.write('Y = %.3f '%(Y))
            result += str(Y)
            x += (max_x - min_x) / (NumberOfSteps - 1)
        print('Минимальное значение G = %.3f' % min(list_three))
        print('Максимальное значение G = %.3f' % max(list_three))
#
    print('Строка: %s' % result)
    template = str(input("Задайте шаблон: "))
    coincidence = result.count(template)  
    print("Совпадений: %s" % coincidence)
    num = int(input("Введите 1 для рассчёта G\nВведите 2 для рассчёта F\nВведите 3 для рассчёта Y\nВведите любую другую цифру для выхода\n"))

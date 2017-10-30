import math

menu = -1
while menu != 4:
    menu = int(input("1: Расчет G\n2: Расчет F\n3: Расчет Y\n4: Выход\n"))
    if menu == 4:
        break
    a = float(input("Введите а: "))
    print("Задайте границы изменения х.")
    min_x = float(input("от: "))
    max_x = float(input("до: "))
    while min_x >= max_x:
        max_x = float(input("Верхняя граница должна быть больше нижней.\nдо: "))
    steps_count = int(input("Введите кол-во шагов: "))
    if menu == 1:
        print("Вычисление G...\n")
        x = min_x
        while x <= max_x:
            den = 25 * math.pow(a, 2) + 30 * a * x + 9 * math.pow(x, 2)
            if den == 0:
                print("x = %.3f\tВходные значения не входят в область определения." % x)
                x += (max_x - min_x) / (steps_count - 1)
                continue
            func = (9 * (7 * math.pow(a, 2) - 19 * a * x + 10 * math.pow(x, 2))) / den
            print("x = %.3f\tG = %.3f" % (x, func))
            x += (max_x - min_x) / (steps_count - 1)
    elif menu == 2:
        print("Вычисление F...\n")
        x = min_x
        while x <= max_x:
            func = math.cos(9 * math.pow(a, 2) - 13 * a * x - 10 * math.pow(x, 2))
            print("x = %.3f\tF = %.3f" % (x, func))
            x += (max_x - min_x) / (steps_count - 1)
    elif menu == 3:
        print("Вычисление Y...\n")
        x = min_x
        while x <= max_x:
            log_value = -80 * math.pow(a, 2) - 46 * a * x + 21 * math.pow(x, 2) + 1
            if log_value <= 0:
                print("x = %.3f\tВходные значения не входят в область определения." % x)
                x += (max_x - min_x) / (steps_count - 1)
                continue
            func = math.log(log_value) / math.log(10)
            print("x = %.3f\tY = %.3f" % (x, func))
            x += (max_x - min_x) / (steps_count - 1)

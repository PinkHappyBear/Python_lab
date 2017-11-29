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
  

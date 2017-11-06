import math
from math import atan

a = float(input("Введите a:"))
b = float(input("Введите b:"))
G = (9 * (20 * (b ** 2) - 31 * a * b + 12 * (b ** 2))) / (10 * (a ** 2) - 17 * a * b + 6 * (b ** 2))
print('A = {}.\nB = {}.\nРезультат: {}'.format(a,b,G))

a = float(input("Введите a:"))
b = float(input("Введите b:"))
F = - atan (7 * (a ** 2) - 2 * a * b - 9 * (b ** 2))
print('A = {}.\nB = {}.\nРезультат: {}'.format(a,b,F))

a = float(input("Введите a:"))
b = float(input("Введите b:"))
Y = - atan (2 * (a ** 2) + (a * b) - 3 * (b ** 2))
print('A = {}.\nB = {}.\nРезультат: {}'.format(a,b,Y))

# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

#
#         *Пример:*
#
#         - 6 -> да
#         - 7 -> да
#         - 1 -> нет

day = int(input("Введите день недели: "))
if day == 6:
    print("Выходной день суббота")
elif day == 7:
    print("Выходной день воскресенье")
else:
    print("Рабочий день")

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Для тех кто пропусти модули с алгоритмами: ¬ - это Отрицание (не); ⋁ - Дизъюнккия (или) ; ⋀ - Конъюнкция (и)
#
""" Не понял условия """

x = int(input("введите число x: "))
y = int(input("введите число y: "))
z = int(input("введите число z: "))

if -(x or y or z) == -x and -y and -z:
    print(True)
else:
    print(False)


# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
#
#                 *Пример:*
#
#         - x=34; y=-30 -> 4
#         - x=2; y=4-> 1
#         - x=-34; y=-30 -> 3

x = int(input("введите число x: "))
y = int(input("введите число y: "))

if x > 0 and y > 0:
    print("принадлежит к первой четверти")
elif x < 0 and y > 0:
    print("точка находится во второй четверти")
elif x < 0 and y < 0:
    print("точка находится в третьей четверти")
elif x > 0 and y < 0:
    print("точка находится в четвертой четверти")


# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
#

number = int(input('Введите номер четверти от 1 до 4: '))
if number == 1:
    print("первая четверть когда x > 0 and y > 0 ")
elif number == 2:
    print("вторая четверть когда x < 0 and y > 0 ")
elif number == 3:
    print("Третья четверть когда x < 0 and y < 0 ")
elif number == 4:
    print("Четвертая четверть когда x > 0 and y < 0 ")


# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt
""" В задаче сказано посчитать растояние в пространстве, добавим высоту  ( Z ) произвольно"""
x_1 = int(input("введите x отрезка А: "))
y_1 = int(input("введите y отрезка А: "))
z_1 = int(input("введите z отрезка А: "))

x_2 = int(input("введите x отрезка B: "))
y_2 = int(input("введите y отрезка B: "))
z_2 = int(input("введите z отрезка B: "))

"""Формула для расчета AB = √(xb - xa)2 + (yb - ya)2 + (zb - za)2 """
result = ((x_2 - x_1)**2) + ((y_2 - y_1)**2) + ((z_2 - z_1)**2)

print(sqrt(result))
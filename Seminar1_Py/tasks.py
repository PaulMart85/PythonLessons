from math import sqrt
from os import system
# Task 1: Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет


def is_weekend(week_day):
    numb = int(week_day)
    if numb<1 or numb>7:
        msg = 'weekday number must be in range of [1;7]'
    else:
        msg = '{} -> {}'.format(numb, numb==6 or numb==7)
    return msg

# Task 2: Напишите программу, которая принимает на вход координаты точки (X и Y), 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3
def which_quadrant(x, y):
    quadr = 1
    if x<0 and y>0: quadr = 2
    elif x<0 and y<0: quadr = 3
    elif x>0 and y<0: quadr = 4
    elif x==0: 
        if y>0: quadr = '+Y'
        else: quadr = '-Y'
    elif y==0:
        if x>0: quadr = '+X'
        else: quadr = '-X'
    return 'x = {}; y = {} -> {}'.format(x, y, quadr)


# Task 3: Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных 
# координат точек в этой четверти (x и y).
def range_of_quadrant(quadr):
    if quadr == 1: rng = 'I: x > 0, y > 0'
    elif quadr == 2: rng = 'II: x < 0, y > 0'
    elif quadr == 3: rng = 'III: x < 0, y < 0'
    elif quadr == 4: rng = 'IV: x > 0, y < 0'
    else: rng = 'number must be in range of [1;4]'

    return rng


# Task 4: Напишите программу, которая принимает на вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
def distance2D(point_1, point_2):
    sq = sqrt( (point_1[0]-point_2[0])**2 + (point_1[1]-point_2[1])**2 )
    return 'A({},{}); B({},{}) -> {:.2f}'.format(point_1[0], point_1[1], point_2[0], point_2[1], sq)


system('cls')
# The solution of the task 1:
print(is_weekend(input('Введите цифру дня недели: ')))

# The solution of the task 2:
print(which_quadrant(float(input('\nВведите координаты точки 2D: \nx = ')), float(input('y = '))))

# The solution of the task 3:
print(range_of_quadrant(int(input('\nВведите номер четверти: '))))

# The solution of the task 4:
p1 = []
p2 = []
p1.append(float(input('\nВведите координаты первой точки:\nX1 = ')))
p1.append(float(input('Y1 = ')))
p2.append(float(input('Введите координаты второй точки:\nX2 = ')))
p2.append(float(input('Y2 = ')))
print(distance2D(p1, p2))
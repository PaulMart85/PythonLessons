# Задача 2: Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Если остается 1 элемент без пары - умножаем его самого на себя.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from os import system
from random import randint


system('cls')

def pair_multiplication(lst):
    res = []
    size = len(lst)
    for i in range(int(0.5*(size + 1))):
        res.append(lst[i] * lst[size-1-i])
    return res


my_list = [2, 3, 4, 5, 6]
print(f'{my_list} => {pair_multiplication(my_list)}')
my_list = [2, 3, 5, 6]
print(f'{my_list} => {pair_multiplication(my_list)}')

my_list = [5]
print(f'{my_list} => {pair_multiplication(my_list)}')
my_list = [randint(-9, 9) for i in range(randint(2, 8))]
print(f'{my_list} => {pair_multiplication(my_list)}')
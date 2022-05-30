# Задача 3: Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19   !!! вероятно, в примере ошибка вывода. 5 => 5.0

from os import system


system('cls')

def diff_max_min(lst):
    res = []
    for index in range(len(lst)):
        res.append(round(lst[index]%1, 2))

    return max(res) - min(res)

my_list = [1.1, 1.2, 3.1, 5, 10.01]
print(f'{my_list} => {diff_max_min(my_list)}')

my_list = [1.1, 1.2, 3.1, 5.05, 10.01]
print(f'{my_list} => {diff_max_min(my_list)}')


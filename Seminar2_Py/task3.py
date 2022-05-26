# Задача 3: Реализуйте случайное перемешивание списка.

# Пример:

# Исходный вариант -> ['Веселый пианист', 250, 3.14, 'True '] 
# Результат -> [250, 3.14, 'True ', 'Веселый пианист']

from os import system
import random

system("cls")

def shuffle_list(l):
    lc = l.copy()
    random.shuffle(lc)
    return lc


list1 = ['Веселый пианист', 250, 3.14, 'True ']
print(f'Исходный вариант -> {list1}')
list2 = shuffle_list(list1)
print(f'Результат -> {list2}\n')
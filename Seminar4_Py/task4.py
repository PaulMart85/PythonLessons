# Задача 4: Задайте два целых числа. Напишите программу, которая найдёт 
# НОК (наименьшее общее кратное) этих двух чисел.

def f(a, b):
    greater = max(a, b)
    while(True):
        if not greater%a and not greater%b: 
            return greater
        greater +=1
    
a = 18
b = 15
print(f'НОК чисел {a} и {b} = {f(a ,b)}')
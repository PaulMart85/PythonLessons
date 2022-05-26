# Задача 2: Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

# Пример:

# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)

from os import system
system("cls")

def mltyply_numbs(N):
    list = []
    list.append(1)
    for i in range(1, N):
        list.append(list[i-1]*(i+1))
    return list


N = 7
print(f'пусть N = {N}, тогда {mltyply_numbs(N)}\n')
# Задача 1: Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр (отсекаем минус, считаем все в плюс).

# Пример:

# 67,82 -> 23
# 0,56 -> 11

from os import system
system("cls")

def sum_of_float(fl, r: int = 0):
    st = str(abs(fl))
    st = st.replace('.', '0')
    for i in range(len(st)):
        r += int(st[i])
    return r



numb = 67.82
print(f'{numb} -> {sum_of_float(numb)}\n')
numb = -0.56
print(f'{numb} -> {sum_of_float(numb)}\n')
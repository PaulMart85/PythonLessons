# Задача 1: Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

def f(list, res = ''):
    for item in reversed(list):
        res += str(item)
    return res

def decimal_to_bynary(numb, list):
    list.append(numb%2)
    if not numb//2: return f(list)
    return decimal_to_bynary(numb//2, list)

numb = 45
print(f'{numb} -> {decimal_to_bynary(numb, [])}\n')
numb = 3
print(f'{numb} -> {decimal_to_bynary(numb, [])}\n')
numb = 2
print(f'{numb} -> {decimal_to_bynary(numb, [])}\n')

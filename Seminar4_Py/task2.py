# Задача 2: Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fibonacci(numb):
    if numb < 0: return (-1)**(-numb + 1) * fibonacci(-numb)
    if numb == 0: return 0
    if numb == 1: return 1
    return fibonacci(numb-1) + fibonacci(numb-2)

numb = 8
print(f'{numb} -> {[fibonacci(i) for i in range(-numb, numb+1)]}\n')

numb = 10
print(f'{numb} -> {[fibonacci(i) for i in range(-numb, numb+1)]}\n')
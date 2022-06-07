# Задача 1: Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 

# *Пример: 

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from os import system
from random import randint
system("cls")


def f_x(i):
    if i==0: return ''
    if i==1: return 'x'
    return 'x^'+str(i)

def f_c(i, k):
    if i==k: return str(randint(1, 3))
    return str(randint(0, 3))

def create_polynom(k):
    list_of_x = [f_x(i) for i in range(k, -1, -1)]
    list_of_coeffs = [f_c(i, k) for i in range(k, -1, -1)]

    polynomial = list(zip(list_of_coeffs, list_of_x))
    res_pol = list(filter(lambda e: e[0] != '0', polynomial))
    polynomial = list(map(lambda e: e[0]+e[1], res_pol))

    st = ' + '.join(polynomial) + ' = 0'
    return st.replace('1x', 'x')

k = 5
pln = create_polynom(k)
with open('out.txt', 'a') as data:
    data.write(f'k={k} => {pln}\n')
    print('Результат записан в файл out.txt')
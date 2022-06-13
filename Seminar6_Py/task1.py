# Задача 1: Даны два файла, в каждом из которых находится запись многочлена. 
# Сформировать файл, содержащий сумму многочленов.

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

def src(i, lst, li = 0):
    sr = f'x^{i} '
    if i == 1: sr = 'x '
    if i == 0: 
        if str(lst[-1]).strip().isdigit(): return int(lst[-1])
        else: return 0
    for l in lst: 
        if sr in l:
            li = str(l).split('x')[0]
            break
    if li=='': li = 1
    return int(li)

def f_s(i, list1, list2):
    return str(src(i, list1) + src(i, list2))


def create_polynom(k):
    list_of_x = [f_x(i) for i in range(k, -1, -1)]
    list_of_coeffs = [f_c(i, k) for i in range(k, -1, -1)]

    polynomial = list(zip(list_of_coeffs, list_of_x))
    res_pol = list(filter(lambda e: e[0] != '0', polynomial))
    polynomial = list(map(lambda e: e[0]+e[1], res_pol))

    st = ' + '.join(polynomial) + ' = 0'
    return st.replace('1x', 'x')

def create_sum_polynom(list1, list2):
    l1 = list1[0].split('^')[1]
    l2 = list2[0].split('^')[1]
    k = int(max(l1, l2))

    list_of_x = [f_x(i) for i in range(k, -1, -1)]
    list_of_coeffs = [f_s(i, list1, list2) for i in range(k, -1, -1)]

    polynomial = list(zip(list_of_coeffs, list_of_x))
    res_pol = list(filter(lambda e: e[0] != '0', polynomial))
    polynomial = list(map(lambda e: e[0]+e[1], res_pol))

    st = ' + '.join(polynomial) + ' = 0'
    return st.replace('1x', 'x')

def write_pol(polinomial, file_name):
    with open(file_name, 'w') as data:
        data.write(polinomial)

def read_pol(file_name):
    with open(file_name, 'r') as data:
        p1 = data.read()
    pol1 = p1.replace('= 0', '')
    return pol1.split('+ ')

# ============================================================
k = 5 # ввод пользователя
pln = create_polynom(k)
write_pol(pln, 'in1.txt') # файл с первым многочленом
print(pln)

k = 3 # ввод пользователя
pln = create_polynom(k)
write_pol(pln, 'in2.txt') # файл со вторым многочленом
print(pln)

list1 = read_pol('in1.txt')
list2 = read_pol('in2.txt')

sum_pln = create_sum_polynom(list1, list2)
write_pol(sum_pln, 'out.txt') # файл с суммой многочленов
print(sum_pln)
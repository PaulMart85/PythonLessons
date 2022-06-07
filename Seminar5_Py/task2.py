# Задача 2: В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

# Данные в файле 'in.txt': {1 8 7 6 2 4 3 9}

from os import system
system("cls")


with open('in.txt', 'r') as data:
    st = data.read()

init_set = set(map(int, st.split()))
print(f'Данные в файле (in.txt): {st}')
help_set = {i for i in range(min(init_set), max(init_set)+1)}
print(f'Недостающее число: {(help_set.difference(init_set)).pop()}')
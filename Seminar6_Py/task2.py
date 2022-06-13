# Реализовать RLE алгоритм. Реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах

from os import system

system('cls')

def compression(data):
    st = '' 
    cnt = 1
    data = data + ' '
    for i in range(len(data)-1):
        if data[i] == data[i + 1]:
            cnt += 1
        else:
            st += str(cnt) + data[i] + ' '
            cnt = 1
    return st

def decompression(st):
    res = ''
    list = str(st).split()
    for item in list:
        res += str(item[-1])*int(item[:-1])
    return res




data = '1111222ffg22223' # ввод пользователя
with open('compress.txt', 'w') as dt:
    dt.write(compression(data))

with open('compress.txt', 'r') as dt:
    st = dt.read()

with open('decompress.txt', 'w') as dt:
    dt.write(decompression(st))

print('Результаты записаны в файлы compress.txt, decompress.txt')
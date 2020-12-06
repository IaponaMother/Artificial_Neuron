import random, numpy as np, math

input_list = []
filter = []
filter2 = []
multiplied_matrices = []
list = []
r = 0
a = int(input("введите количество строк в матрице: "))
b = int(input("введите количество столбцов в матрице: "))

for i in range(a):  # создание первой матрицы
    input_list.append([])
    for j in range(b):
        input_list[i].append(random.randint(0, 10))

for i in input_list:  # вывод первой матрицы
    str1 = " "
    for il in i:
        str1 += str(il) + " "
    print(str1)


for i in range(2):  # создание второй матрицы(фильтра)
    filter.append([])
    for j in range(2):
        filter[i].append(random.randint(0, 1))

print("\n")
for i in filter:  # вывод второй матрицы
    str1 = " "
    for il in i:
        str1 += str(il) + " "
    print(str1)


for i in filter:
    c = i * math.ceil(b / 2)
    filter2.append(c)
filter2 = filter2 * math.ceil(a / 2)

if a % 2 != 0:
    filter2 = np.delete(filter2, 0, axis=0)

if b % 2 != 0:
    filter2 = np.delete(filter2, 0, axis=1)


for i in range(a):  # перемножение элементов матриц
    for il in range(b):
        r = input_list[i][il] * filter2[i][il]
        list.append(r)
    multiplied_matrices.append(list)
    list = []

print("\n")
for i in multiplied_matrices:  # вывод результата
    str1 = " "
    for il in i:
        str1 += str(il) + " "
    print(str1)

a = np.array(filter2)  # с использованием numpy
b = np.array(input_list)
c = a * b
print("с использованием numpy: ", "\n")
print(c)

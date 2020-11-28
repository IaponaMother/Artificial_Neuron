import random, numpy as np

input_list = []
filter = []
filter2 = []
multiplied_matrices = []
list = []
r = 0


for i in range(4):  # создание первой матрицы
    input_list.append([])
    for j in range(4):
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
    a = i * 2
    filter2.append(a)
filter2 = filter2 * 2


for i in range(4):  # перемножение элементов матриц
    for il in range(4):
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
print(c)

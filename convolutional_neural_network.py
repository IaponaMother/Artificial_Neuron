import random

input_list = []
filter = []
filter2 = []
result = []
list = []
r = 0

for i in range(4):  # создание первой матрицы
    input_list.append([])
    for j in range(4):
        input_list[i].append(random.randint(0, 3))
print(input_list)

for i in range(2):  # создание второй матрицы
    filter.append([])
    for j in range(2):
        filter[i].append(random.randint(0, 3))


for i in filter:
    filter2.extend(i)
filter2 = [filter2] * 4
print("\n", filter2)


for il in range(4):  # перемножение матриц
    for j in range(4):
        for i in range(4):
            r = r + input_list[il][i] * filter2[i][j]
        list.append(r)
        r = 0
    result.append(list)
    list = []
print("\n", result)
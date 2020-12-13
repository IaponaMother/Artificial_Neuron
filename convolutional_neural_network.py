import numpy as np

length = int(input("введите длину массива: "))  # создание матрицы
width = int(input("введите ширину массива: "))
input_list = np.random.randint(0, 10, (width, length))
print(input_list)
input_list = np.insert(input_list, 0, values=0, axis=1)  # добаление строк и столбцов в матрицу
input_list = np.insert(input_list, 0, values=0, axis=0)
input_list = np.insert(input_list, length + 1, values=0, axis=1)
input_list = np.insert(input_list, width + 1, values=0, axis=0)
print(input_list)

filter = np.random.randint(0, 2, (3, 3))  # создание фильтра
print(filter)

output_list1 = []
output_list2 = []
i = 1
j = 1
for i in range(width + 1):  # разделяем матрицу на части
    for j in range(length + 1):
        v = input_list[i - 1:i + 2, j - 1:j + 2]
        output_list1.append(v)
    i += 1
    j += 1

for il in output_list1:  # вывод частей матрицы
    print(il)

for il in output_list1:  # свертка матрицы(перемножение и сложение частей матрицы и фильтра)
    if np.shape(il) == (3, 3):
        r = np.sum(il * filter)
        output_list2.append(r)

print(np.array_split(output_list2, width, axis=0))  # вывод получившейся матрицы
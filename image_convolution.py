import numpy as np
from PIL import Image

im = Image.open('sonosharingan.jpg')
matrix = np.array(im)
length = np.shape(matrix)[1]
width = np.shape(matrix)[0]

r, g, b = [], [], []

filter = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
for i in matrix:
    for j in i:
        r.append(j[0])
        g.append(j[1])
        b.append(j[2])

red = np.array_split(r, width, axis=0)
green = np.array_split(g, width, axis=0)
blue = np.array_split(b, width, axis=0)

red = np.insert(red, 0, values=0, axis=1)
red = np.insert(red, 0, values=0, axis=0)
red = np.insert(red, length + 1, values=0, axis=1)
red = np.insert(red, width + 1, values=0, axis=0)

green = np.insert(green, 0, values=0, axis=1)
green = np.insert(green, 0, values=0, axis=0)
green = np.insert(green, length + 1, values=0, axis=1)
green = np.insert(green, width + 1, values=0, axis=0)

blue = np.insert(blue, 0, values=0, axis=1)
blue = np.insert(blue, 0, values=0, axis=0)
blue = np.insert(blue, length + 1, values=0, axis=1)
blue = np.insert(blue, width + 1, values=0, axis=0)

list_red = []
output_list_red = []
list_green = []
output_list_green = []
list_blue = []
output_list_blue = []
i = 1
j = 1
for i in range(width + 1):
    for j in range(length + 1):
        v = red[i - 1:i + 2, j - 1:j + 2]
        t = green[i - 1:i + 2, j - 1:j + 2]
        k = blue[i - 1:i + 2, j - 1:j + 2]
        list_red.append(v)
        list_green.append(t)
        list_blue.append(k)
    i += 1
    j += 1


for il in list_red:
    if np.shape(il) == (3, 3):
        s = np.sum(il * filter)
        output_list_red.append(s)

for il in list_green:
    if np.shape(il) == (3, 3):
        s = np.sum(il * filter)
        output_list_green.append(s)

for il in list_blue:
    if np.shape(il) == (3, 3):
        s = np.sum(il * filter)
        output_list_blue.append(s)

Red = np.array_split(output_list_red, width, axis=0)
Green = np.array_split(output_list_green, width, axis=0)
Blue = np.array_split(output_list_blue, width, axis=0)

rgb = [Red, Green, Blue]
res = np.dstack(rgb)
img = Image.fromarray(res.astype(np.uint8), 'RGB')
img.save('my.png')
img.show()

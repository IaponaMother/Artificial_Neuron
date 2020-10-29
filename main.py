import math, random
b, r = 0, 0


def sigmoid(x):
    return 1 / (1 + math.exp(-x))

inputs = [0, 1, 0]


weights = [random.random() for i in range(len(inputs))]  # weights = [21151, 21151, 21151]

for i in range(200000):
    outputs = sigmoid(1)
    e = 1 - outputs
    r = e * (outputs * e)
    r += r

for i in range(len(weights)):
    weights[i] += r * 200000
print(weights)


for i in range(len(inputs)):
    a = (inputs[i] * weights[i])
    b += a

print(math.floor(sigmoid(b)))

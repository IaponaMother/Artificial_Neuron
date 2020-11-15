import math, random

result, r = 0, 0
inputs = [1, 0, 0]
outputs = 1
weights = [random.random() for i in range(len(inputs))]

def sigmoid(x):
    return 1/(1 + math.exp(-x))

for i in range(len(weights)):
    result += weights[i] * outputs
for i in range(10000):
    o = sigmoid(result)
    e = outputs - o
    r += e * o * (1 - o)

for i in range(len(weights)):
    weights[i] += r * 10000
print(weights)


for i in range(len(inputs)):
    result += inputs[i] * weights[i]
print(round(sigmoid(result)))

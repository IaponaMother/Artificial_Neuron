import math, numpy, random
b = 0
def sigmoid(x):
    return 1/(1 + math.exp(-x))

inputs = [0, 1, 1]

weights = [10575, 10575, 10575]

"""weights = numpy.random.random((3, 1)) 


for i in range(200000):
    outputs = sigmoid(1)
    e = 1 - outputs
    r = e *(outputs *e)
    weights += r
    i += 1

print(weights)"""

for i in range(len(inputs)):
    a = (inputs[i] * weights[i])
    b += a
    i += 1

print(math.floor(sigmoid(b)))
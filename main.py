import numpy

def sigmoid(x):
    return 1/(1 + numpy.exp(-x))

training_inputs = numpy.array([
    [0, 0, 1],
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 1]])

training_outputs = numpy.array([[0, 1, 1, 0]]).T

numpy.random.seed(1)

weights = (13, -0.2, -6.14)

"""print("случайные веса: ")
weights = 2 * numpy.random.random((3, 1)) -1
print(weights)"""


"""for i in range(200000):
    input_layer = training_inputs
    outputs = sigmoid(numpy.dot(input_layer, weights))

    err = training_outputs - outputs
    adjustments = numpy.dot(input_layer.T, err *(outputs *(1 - outputs)))
    weights += adjustments

print("Веса после обучения: ")
print(weights)"""

print("результат после обучения: ")
input_layer = training_inputs
outputs = sigmoid(numpy.dot(input_layer, weights))
print(outputs)

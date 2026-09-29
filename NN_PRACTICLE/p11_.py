import numpy as np 

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

Y = np.array([
    [0],
    [1],
    [1],
    [0]
])


np.random.seed(42)

W1 = np.random.uniform(-1, 1, (2, 4))
b1 = np.zeros((1, 4))

W2 = np.random.uniform(-1, 1, (4, 1))
b2 = np.zeros((1, 1))

learning_rate = 0.5

epochs = 10000

for epoch in range(epochs):


    hidden_input = np.dot(X, W1) + b1
    hidden_output = sigmoid(hidden_input)


    output_input = np.dot(hidden_output, W2) + b2
    output = sigmoid(output_input)




    error = Y - output
    output_delta = error * sigmoid_derivative(output)

    hidden_error = np.dot(output_delta, W2.T)

    # Hidden layer delta
    hidden_delta = hidden_error * sigmoid_derivative(hidden_output)

    W2 += learning_rate * np.dot(hidden_output.T, output_delta)
    b2 += learning_rate * np.sum(output_delta, axis=0, keepdims=True)

    W1 += learning_rate * np.dot(X.T, hidden_delta)
    b1 += learning_rate * np.sum(hidden_delta, axis=0, keepdims=True)


hidden_output = sigmoid(np.dot(X, W1) + b1)
output = sigmoid(np.dot(hidden_output, W2) + b2)

print("Predicted Output:")
print(output)

print("\nRounded Output:")
print(np.round(output))

print("\nActual Output:")
print(Y)
import numpy as np

X=np.array([[0,0],[0,1],[1,0],[1,1]])
Y=np.array([[0],[1],[1],[0]])
np.random.seed(42)

input_neurons = 2
hidden_neurons = 4
output_neurons = 1

learning_rate = 0.5
epochs = 10000

W1 = np.random.randn(input_neurons, hidden_neurons)
b1 = np.zeros((1, hidden_neurons))

W2 = np.random.randn(hidden_neurons, output_neurons)
b2 = np.zeros((1, output_neurons))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

for epoch in range(epochs):
    hidden_input = np.dot(X, W1) + b1
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, W2) + b2
    predicted_output = sigmoid(final_input)

output_error = Y - predicted_output

  
output_delta = (
        output_error *
        sigmoid_derivative(predicted_output)
    )
hidden_error = np.dot(output_delta, W2.T)

hidden_delta = (
        hidden_error *
        sigmoid_derivative(hidden_output)
    )

W2 += (
        learning_rate *
        np.dot(hidden_output.T, output_delta)
    )

b2 += learning_rate * np.sum(
                output_delta,
        axis=0,
        keepdims=True
    )

W1 += (
        learning_rate *
        np.dot(X.T, hidden_delta)
    )

b1 += learning_rate * np.sum(
        hidden_delta,
        axis=0,
        keepdims=True
    )

if (epoch + 1) % 1000 == 0:
        mse = np.mean(output_error ** 2)
        print(
            "Epoch:", epoch + 1,
            "Error:", round(mse, 6)
        )


print("\nXOR Prediction:")

for i in range(len(X)):

    hidden_input = np.dot(X[i:i+1], W1) + b1
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, W2) + b2
    output = sigmoid(final_input)


    result = 1 if output[0][0] >= 0.5 else 0

    print(
        "Input:", X[i],
        "Target:", Y[i][0],
        "Output:", round(output[0][0], 4),
        "Class:", result
    )

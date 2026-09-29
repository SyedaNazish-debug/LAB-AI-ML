import numpy as np
import matplotlib.pyplot as plt

N = 500

M = 4

mu = 0.01

np.random.seed(1)
x = np.random.randn(N)

true_weights = np.array([0.5, -0.3, 0.2, 0.1])

d = np.zeros(N)

for n in range(M, N):
    d[n] = np.dot(true_weights, x[n-M:n])

noise = 0.05 * np.random.randn(N)
d = d + noise

w = np.zeros(M)

y = np.zeros(N)
e = np.zeros(N)

for n in range(M, N):


    x_vector = x[n-M:n]


    y[n] = np.dot(w, x_vector)


    e[n] = d[n] - y[n]


    w = w + mu * e[n] * x_vector

mse = np.mean(e[M:] ** 2)

print("Final Filter Weights:")
print(w)

print("\nMean Square Error:")
print(mse)

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(d, label="Desired Signal")
plt.plot(y, label="LMS Output", alpha=0.8)
plt.title("Desired Signal vs LMS Filter Output")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(e, color="red")
plt.title("LMS Error Signal")
plt.xlabel("Sample")
plt.ylabel("Error")
plt.grid()

plt.tight_layout()
plt.show()
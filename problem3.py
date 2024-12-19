import numpy as np
import matplotlib.pyplot as plt

A = 4
f = 5
t = np.arange(0, 1, 0.01)
x = A * np.sin(2 * np.pi * f * t)

plt.figure(figsize=(8, 6))

# Continuous time signal
plt.subplot(4, 1, 1)
plt.plot(t, x)
plt.title('Continuous time signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)

# Sampling
plt.subplot(4, 1, 2)
plt.stem(t, x)
plt.title('Sampling')
plt.xlabel('Time')
plt.ylabel('Amplitude')

# DC level + discrete time signal
x1 = A + x
plt.subplot(4, 1, 3)
plt.stem(t, x1)
plt.title('Quantization')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)

# Quantization
x2 = np.round(x1)
plt.subplot(4, 1, 4)
plt.stem(t, x2)
plt.title('Coding')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()
# Coding
x3 = np.array([np.binary_repr(int(i)) for i in x2])
print(x3)
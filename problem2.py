import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 1, 1, 1])
N = 4  # for 4-point DFT

plt.figure(figsize=(10, 6))

# Plot the input signal
plt.subplot(2, 1, 1)
plt.stem(np.arange(N), x)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Input Signal')
plt.grid(True)

# DFT computation
y = np.zeros(N, dtype=np.complex128)
for k in range(N):
    for n in range(N):
        y[k] += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)

print("DFT Values:", y)

# Plot the DFT values
plt.subplot(2, 1, 2)
plt.stem(np.arange(N), np.abs(y))
plt.xlabel('k')
plt.ylabel('X(k)')
plt.title('DFT Values')
plt.grid(True)

plt.tight_layout()
plt.show()

x = np.array([4, 0, 0, 0])
N = 4  # for 4-point IDFT

plt.figure(figsize=(10, 6))

# Plot the input signal
plt.subplot(2, 1, 1)
plt.stem(np.arange(N), x)
plt.xlabel('k')
plt.ylabel('x(k)')
plt.title('Input Signal')
plt.grid(True)

# IDFT computation
m = np.zeros(N, dtype=np.complex128)
for n in range(N):
    for k in range(N):
        m[n] += (1/N) * x[k] * np.exp(1j * 2 * np.pi * k * n / N)

print("IDFT Values:", m)

# Plot the IDFT values
plt.subplot(2, 1, 2)
plt.stem(np.arange(N), np.real(m))
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('IDFT Values')
plt.grid(True)

plt.tight_layout()
plt.show()
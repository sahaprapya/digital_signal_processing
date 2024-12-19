import numpy as np
import matplotlib.pyplot as plt
def x(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 1
    else:
        return 0
def h(n):
    if n == -1:
        return 1
    if n == 0:
        return 2
    if n == 1:
        return 1
    if n == 2:
        return -1
    else:
        return 0
time = np.arange(-4, 5, 1)
x= np.array([x(i) for i in time])
h = np.array([h(i) for i in time])
con = np.convolve(x, h, 'full')
cor = np.correlate(x, h, 'full')
plt.figure(figsize=(20, 10))
plt.subplot(2,2, 1)
plt.stem(time, x, label='x(n)')
plt.title("Signal x(n)")

plt.subplot(2,2, 2)
plt.stem(time, h, label='h(n)')
plt.title("Response h(n)")

plt.subplot(2,2, 3)
plt.stem(np.arange(-8, 9, 1),con, label='x(n)*h(n)')
plt.title("Convolution")

plt.subplot(2,2, 4)
plt.stem(np.arange(-8, 9, 1),cor, label='x(n)*h(n)')
plt.title("Correlation")
plt.show()
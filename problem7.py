import matplotlib.pyplot as plt

# Define the input sequence x(n)
x = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]

# Define the output sequence y(n)
n = range(len(x))  # Create a list of indices for x(n)
y = [2 * x[i - 5] - 3 * x[i + 4] if 0 <= i - 5 < len(x) and 0 <= i + 4 < len(x) else 0 for i in n]

# Handle cases where x(n-5) or x(n+4) are out of bounds
for i in range(len(y)):
    if i < 5:
        y[i] = 2 * 0 - 3 * x[i + 4]  # Consider only x(n+4)
    elif i >= len(x) - 4:
        y[i] = 2 * x[i - 5] - 3 * 0  # Consider only x(n-5)

# Plot the sequences
plt.subplot(2, 1, 1)  # Create two rows, one column, first subplot
plt.stem(n, x, label='x(n)')
plt.title('Input Sequence x(n)')

plt.subplot(2, 1, 2)  # Second subplot
plt.stem(n, y, label='y(n)')
plt.title('Output Sequence y(n)')

plt.xlabel('n')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.tight_layout()  # Adjust spacing between subplots
plt.show()
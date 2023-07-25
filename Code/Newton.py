import numpy as np
import matplotlib.pyplot as plt

def divided_differences(x, y):
    n = len(x)
    coef = np.zeros(n)

    for i in range(n):
        coef[i] = y[i]

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])

    return coef

def newton_interpolation(x, y, xi):
    n = len(x)
    coef = divided_differences(x, y)
    result = coef[n - 1]

    for i in range(n - 2, -1, -1):
        result = result * (xi - x[i]) + coef[i]

    return result

# Sample data points
x = np.linspace(-10, 10, 10)
y = 1/(1+x**2)

# Interpolate over a range of x values
xi = np.linspace(-10, 10, 300)
yi = np.zeros_like(xi)

for i in range(len(xi)):
    yi[i] = newton_interpolation(x, y, xi[i])

# Plot the original function and interpolated function

x = np.linspace(-10, 10, 100)
y = 1/(1+x**2)

plt.plot(x, y, 'ro', label='Data Points')
plt.plot(xi, yi, label='Interpolated Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Newton Interpolation of 1/(1+x^2)')
plt.legend()
plt.plot(x,y)
plt.grid()
plt.show()

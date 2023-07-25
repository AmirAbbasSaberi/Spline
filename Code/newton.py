import numpy as np
import matplotlib.pyplot as plt

def divided_differences(x, y):
    n = len(x)
    coefficients = [y[0]]
    for j in range(1, n):
        divided_diff = (y[j] - y[j - 1]) / (x[j] - x[j - 1])
        coefficients.append(divided_diff)
        for i in range(j - 1, 0, -1):
            divided_diff = (coefficients[i] - coefficients[i - 1]) / (x[j] - x[i - 1])
            coefficients[i] = divided_diff
    return coefficients

def newton_interpolation(x, y, xi):
    coefficients = divided_differences(x, y)
    n = len(x)
    result = coefficients[n - 1]
    for i in range(n - 2, -1, -1):
        result = result * (xi - x[i]) + coefficients[i]
    return result

# Generate data points for the function 1/(1+x^2)
x = np.linspace(-10, 10, 40)
y = 1 / (1 + 25*x**2)

# Interpolation
xi = np.linspace(-10, 10, 200)  # Points to evaluate the interpolated polynomial
interpolated_values = [newton_interpolation(x, y, point) for point in xi]

# Plotting
plt.plot(x, y, label='Original Function')
plt.plot(xi, interpolated_values, label='Interpolated Polynomial')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Newtonian Polynomial Interpolation of 1/(1+x^2)')
plt.legend()
plt.grid()
plt.show()

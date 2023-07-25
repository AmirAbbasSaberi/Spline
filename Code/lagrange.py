import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, xi):
    n = len(x)
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (xi - x[j]) / (x[i] - x[j])
        result += term
    return result

# Generate data points for the function 1/(1+x^2)
x = np.linspace(-10, 10, 40)
y = 1 / (1 + x**2)

# Interpolation
xi = np.linspace(-10, 10, 200)  # Points to evaluate the interpolated polynomial
interpolated_values = [lagrange_interpolation(x, y, point) for point in xi]

# Plotting
plt.plot(x, y, label='Original Function')
plt.plot(xi, interpolated_values, label='Interpolated Polynomial')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Polynomial Interpolation of 1/(1+x^2)')
plt.legend()
plt.show()

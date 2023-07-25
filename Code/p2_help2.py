import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Define the variable
x = sp.Symbol('x')

# Define the function
f = 1 / (x**2 + 1)

# Compute the first derivative
f_prime = sp.diff(f, x)

# Compute the second derivative
f_double_prime = sp.diff(f_prime, x)

# Compute the third derivative
f_triple_prime = sp.diff(f_double_prime, x)

# Convert the SymPy expressions to lambda functions for numerical evaluation
f_lambdified = sp.lambdify(x, f)
f_prime_lambdified = sp.lambdify(x, f_prime)
f_double_prime_lambdified = sp.lambdify(x, f_double_prime)
f_triple_prime_lambdified = sp.lambdify(x, f_triple_prime)

# Generate x values for the plot
x_vals = np.linspace(-10, 10, 500)

# Evaluate the functions at x_vals
f_vals = f_lambdified(x_vals)
f_prime_vals = f_prime_lambdified(x_vals)
f_double_prime_vals = f_double_prime_lambdified(x_vals)
f_triple_prime_vals = f_triple_prime_lambdified(x_vals)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_vals, f_vals, label='f(x)')
plt.plot(x_vals, f_prime_vals, label="f'(x)")
plt.plot(x_vals, f_double_prime_vals, label="f''(x)")
plt.plot(x_vals, f_triple_prime_vals, label="f'''(x)")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function $\\frac{1}{1+x^2}$ and its derivatives')
plt.legend()
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Generate data points for the function 1/(1+x^2)
x = np.linspace(-10, 10, 30)
y = 1 / (1 + x**2)
# y = 11*np.power(np.cos(0.5*x),2)  + np.power(x,4)/100 + 7*np.sin(2*x)
# Perform linear spline interpolation
linear_interp = interp1d(x, y, kind='linear')

# Evaluate the interpolated function at points xi
xi = np.linspace(-10, 10, 80)
interpolated_values = linear_interp(xi)

# Plotting
plt.plot(x, y, 'ro', label='Original Function')
plt.plot(xi, interpolated_values, label='Linear Spline Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Spline Interpolation of 1/(1+x^2)')
plt.legend()
plt.grid()
plt.show()

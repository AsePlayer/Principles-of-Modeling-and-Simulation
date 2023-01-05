"""
Project 6: Numeric Computations with Taylor Polynomials
Ryan Scott & Diego Guerra
CST-305
Dr. Ricardo Citro
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import time
import math


# ODEs

# functions return [y', u']
# u[0] = y, u[1] = u


# y'' - 2xy' + x^2y = 0
# u = y'
# u' - 2xu + x^2y = 0

# x = 0, y = 1, y' = -1
def dudx1(u, x):
    return [u[1], 2 * x * u[1] - x ** 2 * u[0]]


# y'' - (x - 2)y' + 2y = 0
# u = y'
# u' - (x - 2)u + 2y = 0

# x = 3, y = 6, y' = 1
def dudx2(u, x):
    return [u[1], (x - 2) * u[1] - 2 * u[0]]


# Computes y's using Taylor Polynomial
# Taylor polynomial of degree 4
def taylor1(x):
    return 1 - x - (1 / 3) * x ** 3 - (1 / 12) * x ** 4


# Taylor polynomial of degree 2
def taylor2(x):
    return 6 + (x - 3) - (11 / 2) * (x - 3) ** 2


def dudx3(u, x):
    return [u[1], 0 * u[1] - (1 / (x ** 2 + 4)) * u[0] + x / (x ** 2 + 4)]


def computer(u, x):
    return [u[1], (- (1/x) + u[1] - u[0] + x)/(x ** 2)]


# Records start time (Odeint 1)
start = time.time()

# Number of points
r = 101
# Start conditions
x = np.linspace(-5, 5, r)
u = [1, -1]

# Calculates with Odeint
uy = odeint(dudx1, u, x)
y = uy[:, 0]

# Calculates time for Odeint 1
t = time.time() - start
print("Odeint 1 operation took ", t, " seconds.")

# Plot results (Odeint 1)
plt.title('Odeint 1')
plt.plot(x, y, label="Odeint 1")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Records start time (Taylor 1)
start = time.time()

# Number of points
r = 101
# Start conditions
x3 = np.linspace(-5, 5, r)

# Calculates with Taylor Polynomial
y3 = taylor1(x3)

# Calculates time for Taylor 1
t = time.time() - start
print("Taylor 1 operation took ", t, " seconds.")

# Plot results (Taylor 1)
plt.title('Taylor 1')
plt.plot(x3, y3, label="Taylor 1", linestyle=":")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Show Odeint and Taylor together
plt.plot(x, y, label="Odeint 1")
plt.plot(x3, y3, label="Taylor 1", linestyle=":")
plt.legend()
plt.show()

# Records start time (Odeint 2)
start = time.time()

# Number of points
r = 101
# Start conditions
x2 = np.linspace(0, 6, r)
u2 = [6, 1]

# Calculates with Odeint
uy2 = odeint(dudx2, u2, x2)
y2 = uy2[:, 0]

# Calculates time for Odeint 2
t = time.time() - start
print("Odeint 2 operation took ", t, " seconds.")

# Plot results (Odeint2)
plt.title('Odeint 2')
plt.plot(x2, y2, label="Odeint 2")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Records start time (Taylor 2)
start = time.time()

# Number of points
r = 101
# Start conditions
x4 = np.linspace(0, 6, r)

# Calculates with Taylor Polynomial
y4 = taylor2(x4)

# Calculates time for Taylor 2
t = time.time() - start
print("Taylor 2 operation took", t, "seconds.")

# Plot results (Taylor 2)
plt.title('Taylor 2')
plt.plot(x4, y4, label="Taylor 2", linestyle=":")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Show Odeint and Taylor together
plt.plot(x2, y2, label="Odeint 2")
plt.plot(x4, y4, label="Taylor 2", linestyle=":")
plt.legend()
plt.show()

# Records start time (Odeint 3)
start = time.time()

# Number of points
r = 101
# Start conditions
x3 = np.linspace(0, 10, r)
u3 = [0, 0]

# Calculates with Odeint
uy3 = odeint(dudx3, u3, x3)
y3 = uy3[:, 0]

# Calculates time for Odeint 2
t = time.time() - start
print("Odeint 3 operation took", t, "seconds.")

# Plot results (Odeint 2)
plt.title('Odeint 3')
plt.plot(x3, y3, label="Odeint 3")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Records start time (CPU)
start = time.time()

# Number of points
r = 101
# Start conditions
xc = np.linspace(1, 30, r)
uc = [0, 0]

# Calculates with Odeint
uyc = odeint(computer, uc, xc)
yc = uyc[:, 0]

# Calculates time for CPU
t = time.time() - start
print("CPU operation took", t, "seconds.")

# Plot results (CPU)
plt.title('Computer')
plt.plot(xc, yc, label="Computer")
plt.xlabel('Cost')
plt.ylabel('Best performance')
plt.legend()
plt.show()

